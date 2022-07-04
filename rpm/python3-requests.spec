Name:       python3-requests
Summary:    Requests is an elegant and simple HTTP library for Python
Version:    2.23.0
Release:    1
License:    ASL 2.0
URL:        https://github.com/sailfishos/python3-requests
BuildArch:  noarch
Source0:    %{name}-%{version}.tar.bz2
Requires:   python3-base
Requires:   python3-certifi >= 2017.4.17
Requires:   python3-chardet >= 3.0.2
Requires:   python3-idna >= 2.5
Requires:   python3-urllib3 >= 1.25.2
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-chardet
BuildRequires:  python3-idna
BuildRequires:  python3-pygments
BuildRequires:  python3-urllib3

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
%{python3_sitelib}/requests
%{python3_sitelib}/requests-*.egg-info
