%define	name	ldapscripts
%define	version	1.6
%define	release	%mkrel 1

Name        : %name
Version     : %version
Release     : %release
Group       : System/Servers
License     : GPL
Source      : http://contribs.martymac.com/ldapscripts/%{name}-%{version}.tar.bz2
URL         : http://contribs.martymac.com/
Summary     : LDAP Scripts
Requires    : openldap openldap-clients sharutils
Buildarch   : noarch
BuildRoot   : %{_tmppath}/%{name}-buildroot

%description
LDAP Scripts written in bash which allow to create POSIX entries for users,
groups and machines in an LDAP directory.

They are similar to smbldap-tools but are written in sh instead of PERL and
only require OpenLDAP client commands (ldapadd, ldapdelete, ldapsearch,
ldapmodify, slappasswd).

%prep
%setup -q
sed -i.orig -e "s|^_RUNTIMEFILE=.*|_RUNTIMEFILE=\"%{_sysconfdir}/%{name}/runtime\"|g" bin/*
sed -i.orig -e "s|^_CONFIGFILE=.*|_CONFIGFILE=\"%{_sysconfdir}/%{name}/ldapscripts.conf\"|g" etc/*

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 755 bin/* $RPM_BUILD_ROOT%{_bindir}

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
install -m 600 etc/* $RPM_BUILD_ROOT%{_sysconfdir}/%{name}

mkdir -p $RPM_BUILD_ROOT%{_mandir}
cp -a man/man* $RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README COPYING CHANGELOG 
%{_bindir}/*
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%{_sysconfdir}/%{name}/*.template.sample
%{_sysconfdir}/%{name}/runtime
%{_mandir}/man*/*

