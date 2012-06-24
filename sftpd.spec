# TODO:
# - missing userdel
# - safetp-client subpackage
# - rc-inetd file (subpackage)
# - maybe prepare packages for each ftp server???
# - init file (subpackage)
Summary:	SafeTP Transparent FTP Security Software
Summary(pl):	SafeTP - przezroczyste bezpiecze�stwo dla FTP
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

%description -l pl
SafeTP to nowa rewolucyjna aplikacja zabezpieczaj�ca dla u�ytkownik�w
Windows i uniks�w korzystaj�cych z FTP (File Transfer Protocol) do
��czenia si� z kontami na serwerach uniksowych lub NT/2000. Tradycyjny
protok� FTP jest bardzo niebezpieczny: wysy�a has�a czystym tekstem.
Z tego powodu FTP jest uznawany za jeden z wi�kszych problem�w
bezpiecze�stwa w wi�kszo�ci system�w uniksowych.

G��wn� zalet� SafeTP jest przezroczysto��. Kiedy SafeTP jest
zainstalowany, dowolny windowsowy klient FTP staje si� klientem Secure
FTP, bez �adnej dalszej interwencji u�ytkownika. SafeTP przechwytuje
wychodz�ce po��czenia FTP i koduje ca�y ruch przed przekazaniem go do
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
