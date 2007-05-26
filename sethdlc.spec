# TODO: integrate hdlc support into rc-scripts, drop sethdlc.init from doc
#
Summary:	Tool for synchronous cards
Summary(pl.UTF-8):	Narzędzie do konfiguracji kart synchronicznych
Name:		sethdlc
Version:	1.18
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://www.kernel.org/pub/linux/utils/net/hdlc/%{name}-%{version}.tar.gz
# Source0-md5:	9016878156a5eadb06c0bae71cc5c9ab
Source1:	%{name}.init
Patch0:		%{name}-tahoe.patch
URL:		http://www.kernel.org/pub/linux/utils/net/hdlc/
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tool for synchronous cards.

%description -l pl.UTF-8
Narzędzie do konfiguracji kart synchronicznych.

%prep
%setup -q
%patch0 -p1

cp %{SOURCE1} .
rm -f sethdlc

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"\
	INCLUDES=

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install sethdlc $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc sethdlc.init
%attr(755,root,root) %{_sbindir}/sethdlc
