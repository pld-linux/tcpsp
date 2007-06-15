Summary:	tcpsp - TCP Splicing tool
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
TCPSP implements tcp splicing for the Linux kernel. The tcp splicing is a
technique to splice two connections inside the kernel, so that data
relaying between the two connections can be run at near router speeds.
This technique can be used to speed up layer-7 switching, web proxy and
application firewall running in the user space.

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
