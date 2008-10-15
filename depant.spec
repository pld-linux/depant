Summary:	(DE)fault (PA)ssword (N)etwork (T)ool
Summary(pl.UTF-8):	Narzędzie do sprawdzania haseł w sieci
Name:		depant
Version:	0.3a
Release:	0.1
License:	GPL v2
Group:		Applications/Console
Source0:	http://midnightresearch.com/local/packages/depant/%{name}-%{version}.tgz
# Source0-md5:	d1f7af5228436ff1d3816dffd1f2e458
URL:		http://midnightresearch.com/
BuildRequires:	python >= 1:2.5
BuildRequires:	python-setuptools
Requires:	hydra >= 5.4
Requires:	python-ipcalc
Requires:	nmap
%pyrequires_eq	python-libs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Depant works by downloading a default password list, and then mapping
out the local network to see what open services are available. Once it
has a list of services, it will test each service for default
passwords. Once it’s gone through each of the services, depant will
determine the fastest service (as recorded in phase one) and use it to
perform an optional second phase of tests with a larger
(user-supplied) set of default users/passwords.

%description -l pl.UTF-8
Depant działa w ten sposób, że pobiera listę domyślnych haseł, a potem
skanuje sieć w poszukiwaniu uruchomionych usług. Po zakończeniu
poszukiwań każdy znaleziony serwis jest sprawdzany pod kątem
występowania domyślnych haseł. W czasie trwania tej fazy depant
określa również, która usługa jest najszybsza i na tej podstawie
możliwe jest opcjonalne przeprowadzenie fazy drugiej gdzie dany serwis
jest sprawdzany pod kątem haseł dostarczonych przez użytkownika.

%prep
%setup -q -n %{name}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--prefix=%{_prefix} \
	--install-scripts=%{_bindir} \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL LICENSE README
%attr(755,root,root) %{_bindir}/depant
%{py_sitescriptdir}/depant
%{py_sitescriptdir}/Depant-*.egg-info
