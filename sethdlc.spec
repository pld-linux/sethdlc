#
# Conditional build:
%bcond_with     tahoe	# - build sethdlc for tahoe (special version)
#
%define		_ver	1.15
Summary:	Tool for synchronous cards
Summary(pl):	Narzêdzie do konfiguracji kart synchronicznych
Name:		sethdlc
Version:	1.1%{?with_tahoe:6t}%{!?with_tahoe:5}
Release:	3
License:	GPL
Group:		Networking/Utilities
Source0:	http://hq.pm.waw.pl/hdlc/%{name}-%{_ver}.tar.gz
# Source0-md5:	3bc714ee98e6215e8560598ff1e1eb8f
Source1:	%{name}.init
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
if [ -r /var/lock/subsys/sethdlc ]; then
        /etc/rc.d/init.d/sethdlc restart >&2
else
        echo "Run \"/etc/rc.d/init.d/sethdlc start\" to start TPNET Frame Relay."
fi

%preun
if [ "$1" = "0" ]; then
        if [ -r /var/lock/subsys/sethdlc ]; then
                /etc/rc.d/init.d/sethdlc stop >&2
        fi
        /sbin/chkconfig --del sethdlc
fi
%endif

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/sethdlc
%if %{with tahoe}
%attr(755,root,root) /etc/rc.d/init.d/sethdlc
%endif
