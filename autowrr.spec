Summary:	Program that can help you configuring WRR queue
Summary(pl.UTF-8):	Program ułatwiający konfigurowanie kolejki WRR
Name:		autowrr
Version:	0.5a
Release:	1
License:	GPL
Group:		Networking/Admin
Source0:	http://autowrr.olgroup.net/download/%{name}-%{version}.tar.gz
# Source0-md5:	0b5504df84fc0deb932e5bf2c907bcef
URL:		http://autowrr.olgroup.net/
BuildRequires:	cdk-devel
BuildRequires:	ncurses-devel
Requires:	firewall-userspace-tool
Requires:	gawk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description 
AutoWRR is a program that can help you to configure WRR queue
optimally, i.e.:
- put ICMP (incl. ping) in priority class
- specify ports to put in priority class
- use SFQ queue beside WRR to fairly divide bandwidth between
  connections from one host.

%description -l pl.UTF-8
AutoWRR jest w zasadzie programem mającym pomagać optymalnie
skonfigurować kolejkę WRR. Optymalna konfiguracja tzn.:
- Protokół ICMP (min. ping) w klasie priorytetowej
- Możliwość określenia portów mających być również w klasie
  priorytetowej
- Poza WRR użyta jeszcze została kolejka SFQ - w celu sprawiedliwego
  podziału prędkości połączeń dla jednego komputera

%prep
%setup -q

%build
%configure
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}/autowrr,/etc/rc.d/init.d}

install autowrr $RPM_BUILD_ROOT%{_bindir}
install autowrr-wizard $RPM_BUILD_ROOT%{_bindir}
install wrr $RPM_BUILD_ROOT/etc/rc.d/init.d
install start.sh $RPM_BUILD_ROOT%{_sysconfdir}/autowrr
install stop.sh $RPM_BUILD_ROOT%{_sysconfdir}/autowrr
install htb $RPM_BUILD_ROOT%{_sysconfdir}/autowrr
install cbq $RPM_BUILD_ROOT%{_sysconfdir}/autowrr

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changelog TODO
%dir %{_sysconfdir}/autowrr
%attr(755,root,root) %{_sysconfdir}/autowrr/*
%attr(755,root,root) %{_bindir}/*
%attr(754,root,root) /etc/rc.d/init.d/wrr
