# TODO:
# - Summary, desc, cleanups, 
# - with bcond tahoe check with kernel-headers with tahoe patch,
# - check this one vs khc's generic sethdlc - is it Tahoe-specific?

# Conditional build
%bcond_with     tahoe	# - build sethdlc for tahoe
%define		_ver	1.15
Summary:	Tool for synchronous cards
Summary(pl):	Narzêdzie do konfiguracji kart synchronicznych
Name:		sethdlc
Version:	1.1%{?_with_tahoe:6t}%{!?_with_tahoe:5}
Release:	2
License:	GPL
Group:		Networking/Utilities
Source0:	http://hq.pm.waw.pl/hdlc/%{name}-%{_ver}.tar.gz
# Source0-md5:	3bc714ee98e6215e8560598ff1e1eb8f
Patch0:		%{name}-tahoe.patch
URL:		http://hq.pm.waw.pl/hdlc/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tool for synchronous cards.

%description -l pl
Narzêdzie do konfiguracji kart synchronicznych.

%prep
%setup -q -n %{name}-%{_ver}
%if %{with tahoe}
%patch -p1
%endif

%build
echo %{version}
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"\
%if !%{with tahoe}
	INCLUDES=""
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install sethdlc $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/sethdlc
