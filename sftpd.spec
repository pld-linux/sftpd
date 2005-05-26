Summary:	SafeTP Transparent FTP Security Software
Name:		sftpd
Version:	1.50
Release:	0.1
License:	GPL
Group:		Applications/Networking
Source0:	http://safetp.cs.berkeley.edu/tmp-location//%{name}-%{version}.tar.gz
# Source0-md5:	a01338b4e0a13692ed893d067f115d75
Patch0:		%{name}-dynamic_gmp.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gmp-devel
URL:		http://safetp.cs.berkeley.edu/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SafeTP is a revolutionary new security application for Windows and
UNIX users who use FTP (File Transfer Protocol) to connect to their
accounts on UNIX or NT/2000 FTP servers. The traditional FTP protocol
is highly insecure: it sends passwords in the clear. For this reason
FTP has been recognized as one of the largest remaining security
liabilities in most UNIX systems.

The key advantage of SafeTP is transparency. When SafeTP is installed,
any ordinary Windows FTP client automatically becomes a Secure FTP
client, without any further user intervention. SafeTP intercepts
outgoing FTP network connections, and encrypts the traffic before
relaying it to the network.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

#mv $RPM_BUILD_ROOT%{_bindir}/sftp \
#	$RPM_BUILD_ROOT%{_bindir}/sftpc
#mv $RPM_BUILD_ROOT%{_mandir}/man1/sftp.1 \
#	$RPM_BUILD_ROOT%{_mandir}/man1/sftpc.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
#%doc README Changelog
#%attr(755,root,root) %{_bindir}/*
#%{_mandir}/man?/*