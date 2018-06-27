%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%define proj_name networkx

Name:           python-%{proj_name}
Version:        1.9.2
Release:        0%{?dist}
Summary:        simpleutil copy from openstack
Group:          Development/Libraries
License:        MPLv1.1 or GPLv2
URL:            http://github.com/Lolizeppelin/%{proj_name}
Source0:        %{proj_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  python-setuptools >= 11.0

Requires:       python >= 2.6.6
Requires:       python < 2.7
Requires:       python-decorator >= 3.4.0


%description
utils copy from openstack


%prep
%setup -q -n %{proj_name}-%{version}


%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
%dir %{python_sitelib}/%{proj_name}*
%{python_sitelib}/%{proj_name}*/*
%doc *.txt
%doc examples

%changelog

* Sun Sep 9 2017 Lolizeppelin <lolizeppelin@gmail.com> - 1.9.2
- Add node_dict_factory adjlist_dict_factory edge_attr_dict_factory work like 1.10
- Clone from https://pypi.python.org/pypi/networkx/1.9.1
- https://github.com/networkx/networkx/