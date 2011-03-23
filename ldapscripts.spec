%define	name	ldapscripts
%define	version	1.10.0
%define	release	%mkrel 1

Name:       %name
Version:    %version
Release:    %release
Summary:    LDAP Scripts
Group:      System/Servers
License:    GPL
URL:        http://contribs.martymac.com/
Source:     http://contribs.martymac.com/ldapscripts/%{name}-%{version}.tgz
Requires:   openldap-clients
Requires:   sharutils
Buildarch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
LDAP Scripts written in bash which allow to create POSIX entries for users,
groups and machines in an LDAP directory.

They are similar to smbldap-tools but are written in sh instead of PERL and
only require OpenLDAP client commands (ldapadd, ldapdelete, ldapsearch,
ldapmodify, slappasswd).

%prep
%setup -q
sed -i.orig -e "s|^_RUNTIMEFILE=.*|_RUNTIMEFILE=\"%{_usr}/lib/%{name}/runtime\"|g" sbin/*
sed -i.orig -e "s|^_CONFIGFILE=.*|_CONFIGFILE=\"%{_sysconfdir}/%{name}/ldapscripts.conf\"|g" etc/* lib/*

%install
mkdir -p %{buildroot}%{_sbindir}
install -m 755 sbin/* %{buildroot}%{_sbindir}

mkdir -p %{buildroot}%{_sysconfdir}/%{name}
install -m 600 etc/* %{buildroot}%{_sysconfdir}/%{name}

mkdir -p %{buildroot}%{_usr}/lib/%{name}
install -m 600 lib/* %{buildroot}%{_usr}/lib/%{name}

mkdir -p %{buildroot}%{_mandir}
cp -a man/man* %{buildroot}%{_mandir}

%clean
rm -rf %{buildroot}

%files
%doc README COPYING CHANGELOG 
%{_sbindir}/*
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.passwd
%{_sysconfdir}/%{name}/*.template.sample
%{_usr}/lib/%{name}/runtime
%{_mandir}/man*/*

