Summary:	Program u�atwiaj�cy konfigurowanie kolejki WRR
Summary(pl):	Program that can help you configuring WRR queue
Name:		autowrr
Version:	0.5a
Release:	1
License:	GPL
Group:		Networking/Admin
Source0:	http://autowrr.olgroup.net/download/%{name}-%{version}.tar.gz
URL:		http://autowrr.olgroup.net/
Requires:	firewall-userspace-tool
Requires:	ncurses
Requires:	gawk
Requires:	cdk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description 
AutoWRR is a program that can help you configuring WRR queue.

%description -l pl
AutoWRR jest w zasadzie programem maj�cym pomaga� optymalnie
skonfigurowa� kolejk� WRR. Optymalna konfiguracja tzn:

    - Protok� ICMP (min. ping) w klasie priorytetowej
    - Mo�liwo�� okre�lenia port�w maj�cych by� r�wnie� w klasie
      priorytetowej
    - Poza WRR u�yta jeszcze zosta�a kolejka SFQ - w celu sprawiedliwego
      podzia�u pr�dko�ci po��cze� dla jednego komputera

%prep
%setup -q

%build
%configure
%{__make} \
        CC="%{__cc}" \
        CFLAGS="%{rpmcflags}"


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}/{autowrr,rc.d/init.d}}

install autowrr $RPM_BUILD_ROOT%{_bindir}
install autowrr-wizard $RPM_BUILD_ROOT%{_bindir}
install wrr $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d/
install start.sh $RPM_BUILD_ROOT%{_sysconfdir}/autowrr/
install stop.sh $RPM_BUILD_ROOT%{_sysconfdir}/autowrr/
install htb $RPM_BUILD_ROOT%{_sysconfdir}/autowrr/
install cbq $RPM_BUILD_ROOT%{_sysconfdir}/autowrr/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changelog TODO
%dir %{_sysconfdir}/autowrr
%attr(755,root,root) %{_sysconfdir}/autowrr/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sysconfdir}/rc.d/init.d/wrr
