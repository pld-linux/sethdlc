# TODO:
# - Summary, desc, cleanups, 
# - with bcond tahoe check with kernel-headers with tahoe patch,
# - check this one vs khc's generic sethdlc - is it Tahoe-specific?

# Conditional build
%bcond_with     tahoe	# - build sethdlc for tahoe
Summary:	Tool for synchronous cards
Summary(pl):	Narzêdzie do konfiguracji kart synchronicznych
Name:		sethdlc
Version:	1.15
Release:	0.1
License:	GPL
Group:		Networking/Utilities
Source0:	http://hq.pm.waw.pl/hdlc/%{name}-%{version}.tar.gz
# Source0-md5:	3bc714ee98e6215e8560598ff1e1eb8f
Patch0:		%{name}-tahoe.patch
URL:		http://hq.pm.waw.pl/hdlc/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tool for synchronous cards.

%description -l pl
Narzêdzie do konfiguracji kart synchronicznych.

%prep
%setup -q
%if %{with tahoe}
%patch -p1
%endif

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install sethdlc $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sethdlc
