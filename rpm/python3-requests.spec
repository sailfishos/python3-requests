Name:       python3-requests
Summary:    Requests is an elegant and simple HTTP library for Python
Version:    2.23.0
Release:    1
License:    ASL 2.0
URL:        https://pypi.org/project/requests/
BuildArch:  noarch
Source0:    %{name}-%{version}.tar.bz2
Requires:   python3-base
Requires:   python3-certifi >= 2017.4.17
Requires:   python3-chardet >= 3.0.2, python3-chardet < 4
Requires:   python3-idna >= 2.5, python3-idna < 3
Requires:   python3-urllib3 >= 1.21.1, python3-urllib3 < 1.26
Conflicts:  python3-urllib3 == 1.25.0, python3-urllib3 == 1.25.1
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Requests allows you to send HTTP/1.1 requests extremely easily. There’s no need to manually add query strings to your URLs, or to form-encode your PUT & POST data — but nowadays, just use the json method!

%prep
%setup -q -n %{name}-%{version}/requests

%build
%{py3_build}

%install
rm -rf %{buildroot}
%{py3_install}

%files
%defattr(-,root,root,-)
%{python3_sitearch}/requests
%{python3_sitearch}/requests-*.egg-info
