Name:       ldapscripts
Version:    2.0.8
Release:    1
Summary:    LDAP Scripts
Group:      System/Servers
License:    GPL
URL:        https://contribs.martymac.com/
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



%changelog
* Wed Mar 23 2011 Lev Givon <lev@mandriva.org> 1.10.0-1mdv2011.0
+ Revision: 648174
- Update to 1.10.0.

* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.7.1-5mdv2011.0
+ Revision: 620061
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.7.1-4mdv2010.0
+ Revision: 429708
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 1.7.1-3mdv2009.0
+ Revision: 248332
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Dec 07 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.7.1-1mdv2008.1
+ Revision: 116161
- new version

* Sat Nov 17 2007 Funda Wang <fwang@mandriva.org> 1.6-2mdv2008.1
+ Revision: 109223
- rebuild for new lzma

* Mon May 07 2007 Andreas Hasenack <andreas@mandriva.com> 1.6-1mdv2008.0
+ Revision: 24960
- updated to version 1.6
- the runtime file is not a config file


* Tue Jan 16 2007 Pascal Terjan <pterjan@mandriva.org> 1.5-1mdv2007.0
+ Revision: 109466
- 1.5

* Tue Dec 19 2006 Pascal Terjan <pterjan@mandriva.org> 1.4-1mdv2007.1
+ Revision: 100250
- handle new files
- 1.4
- Import ldapscripts

* Sat Feb 18 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.3-2mdk
- Fix Build

* Sun Oct 09 2005 Pascal Terjan <pterjan@mandriva.org> 1.3-1mdk
- 1.3

* Fri Sep 16 2005 Pascal Terjan <pterjan@mandriva.org> 1.2-1mdk
- First Mandriva release

