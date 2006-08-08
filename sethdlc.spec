#
# Conditional build:
%bcond_with	tahoe	# - build sethdlc for tahoe (special version)
#
%define		_ver	1.15
Summary:	Tool for synchronous cards
Summary(pl):	Narzêdzie do konfiguracji kart synchronicznych
Name:		sethdlc
Version:	1.1%{?with_tahoe:6t}%{!?with_tahoe:5}
Release:	3
License:	GPL
Group:		Networking/Utilities
Source0:	http://www.kernel.org/pub/linux/utils/net/hdlc/%{name}-%{_ver}.tar.gz
# Source0-md5:	3bc714ee98e6215e8560598ff1e1eb8f
Source1:	%{name}.init
Patch0:		%{name}-tahoe.patch
URL:		http://www.kernel.org/pub/linux/utils/net/hdlc/
BuildRequires:	rpmbuild(macros) >= 1.268
%if %{with tahoe}
Requires(post,preun):	/sbin/chkconfig
Requires:	rc-scripts
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tool for synchronous cards.

%description -l pl
Narzêdzie do konfiguracji kart synchronicznych.

%prep
%setup -q -n %{name}-%{_ver}
%if %{with tahoe}
%patch0 -p1
%endif

%build
echo %{version}
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"\
%if %{without tahoe}
	INCLUDES=""
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},/etc/rc.d/init.d}

install sethdlc $RPM_BUILD_ROOT%{_sbindir}
%if %{with tahoe}
install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/sethdlc
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with tahoe}
%post
/sbin/chkconfig --add sethdlc
%service sethdlc restart "TPNET Frame Relay"

%preun
if [ "$1" = "0" ]; then
	%service sethdlc stop
	/sbin/chkconfig --del sethdlc
fi
%endif

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/sethdlc
%if %{with tahoe}
%attr(754,root,root) /etc/rc.d/init.d/sethdlc
%endif
