# TODO:
# - Summary, desc, cleanups, check with kernel-headers with tahoe patch,
# - check this one vs khc's generic sethdlc - is it Tahoe-specific?
Summary:	Tool for Tahoe synchronous cards
Summary(pl):	Narzêdzie do konfiguracji kart synchronicznych Tahoe
Name:		sethdlc
Version:	1.16t
Release:	0.1
License:	GPL
Group:		Networking/Utilities
Source0:	http://www.tahoe.pl/hdlc/%{name}-1.16t.tar.gz
# Source0-md5:	82fe859700e928c22c531a9467fb405b
URL:		http://www.tahoe.pl/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tool for Tahoe synchronous cards.

%description -l pl
Narzêdzie do konfiguracji kart synchronicznych Tahoe.

%prep
%setup -q

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
