%define	name	ldapscripts
%define	version	1.7.1
%define	release	%mkrel 1

Name:       %name
Version:    %version
Release:    %release
Summary:    LDAP Scripts
Group:      System/Servers
License:    GPL
URL:        http://contribs.martymac.com/
Source:     http://contribs.martymac.com/ldapscripts/%{name}-%{version}.tar.bz2
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
sed -i.orig -e "s|^_RUNTIMEFILE=.*|_RUNTIMEFILE=\"%{_sysconfdir}/%{name}/runtime\"|g" bin/*
sed -i.orig -e "s|^_CONFIGFILE=.*|_CONFIGFILE=\"%{_sysconfdir}/%{name}/ldapscripts.conf\"|g" etc/*

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 bin/* %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_sysconfdir}/%{name}
install -m 600 etc/* %{buildroot}%{_sysconfdir}/%{name}

mkdir -p %{buildroot}%{_mandir}
cp -a man/man* %{buildroot}%{_mandir}

%clean
rm -rf %{buildroot}

%files
%doc README COPYING CHANGELOG 
%{_bindir}/*
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.passwd
%{_sysconfdir}/%{name}/*.template.sample
%{_sysconfdir}/%{name}/runtime
%{_mandir}/man*/*

