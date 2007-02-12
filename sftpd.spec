# TODO:
# - missing userdel
# - safetp-client subpackage
# - rc-inetd file (subpackage)
# - maybe prepare packages for each ftp server???
# - init file (subpackage)
Summary:	SafeTP Transparent FTP Security Software
Summary(pl.UTF-8):	SafeTP - przezroczyste bezpieczeństwo dla FTP
Name:		sftpd
Version:	1.50
Release:	0.1
License:	non distributable (see license.txt)
Group:		Applications/Networking
Source0:	http://safetp.cs.berkeley.edu/tmp-location//%{name}-%{version}.tar.gz
# NoSource0-md5:	a01338b4e0a13692ed893d067f115d75
NoSource:	0
Patch0:		%{name}-dynamic_gmp.patch
URL:		http://safetp.cs.berkeley.edu/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gmp-devel
BuildRequires:	rpmbuild(macros) >= 1.202
Provides:		user(safetp)
Requires(pre):	/bin/id
Requires(pre):	/usr/sbin/useradd
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

%description -l pl.UTF-8
SafeTP to nowa rewolucyjna aplikacja zabezpieczająca dla użytkowników
Windows i uniksów korzystających z FTP (File Transfer Protocol) do
łączenia się z kontami na serwerach uniksowych lub NT/2000. Tradycyjny
protokół FTP jest bardzo niebezpieczny: wysyła hasła czystym tekstem.
Z tego powodu FTP jest uznawany za jeden z większych problemów
bezpieczeństwa w większości systemów uniksowych.

Główną zaletą SafeTP jest przezroczystość. Kiedy SafeTP jest
zainstalowany, dowolny windowsowy klient FTP staje się klientem Secure
FTP, bez żadnej dalszej interwencji użytkownika. SafeTP przechwytuje
wychodzące połączenia FTP i koduje cały ruch przed przekazaniem go do
sieci.

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
install -d $RPM_BUILD_ROOT/etc/safetp

#%{__make} install \
#	DESTDIR=$RPM_BUILD_ROOT

#mv $RPM_BUILD_ROOT%{_bindir}/sftp \
#	$RPM_BUILD_ROOT%{_bindir}/sftpc
#mv $RPM_BUILD_ROOT%{_mandir}/man1/sftp.1 \
#	$RPM_BUILD_ROOT%{_mandir}/man1/sftpc.1

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%useradd -u 135 -r -d /home/services/safetp -s /bin/false -c "SafeTP proxy user" -g daemon safetp

%files
%defattr(644,root,root,755)
%doc *.txt
#%doc README Changelog
#%attr(755,root,root) %{_bindir}/*
#%{_mandir}/man?/*
