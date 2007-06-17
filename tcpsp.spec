# TODO: optflags
Summary:	tcpsp - TCP Splicing tool
Summary(pl.UTF-8):	tcpsp - narzędzie do TCP Splicingu
Name:		tcpsp
Version:	0.0.5
Release:	0.1
License:	GPL v2
Group:		Applications/Networking
Source0:	http://www.linuxvirtualserver.org/software/tcpsp/%{name}-%{version}.tar.gz
# Source0-md5:	e2ddde26a93bde0c31dacf8547c9cd94
URL:		http://www.linuxvirtualserver.org/software/tcpsp/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TCPSP implements TCP splicing for the Linux kernel. The TCP splicing
is a technique to splice two connections inside the kernel, so that
data relaying between the two connections can be run at near router
speeds. This technique can be used to speed up layer-7 switching, web
proxy and application firewall running in the user space.

%description -l pl.UTF-8
TCPSP implementuje TCP Splicing (splatanie TCP) dla jądra Linuksa.
TCP Splicing to technika splatania dwóch połączeń wewnątrz jądra tak,
żeby dane przesyłane między dwoma połączeniami mogły wędrować z
prędkościami bliskimi routera. Technika ta może być używana do
przyspieszenia przełączania w warstwie 7, w proxy WWW oraz firewallach
aplikacji działających w przestrzeni użytkownika.

%prep
%setup -q -n %{name}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
#%attr(755,root,root) %{_bindir}/*
#%{_mandir}/man1/*
