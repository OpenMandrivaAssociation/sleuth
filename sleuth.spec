Summary:	Perl script for easy checking (DNS, common errors and etc.)
Name:		sleuth
Version:	1.4.3
Release:	%mkrel 5
License:	GPL
Group:		Networking/Other
URL:		ftp://atrey.karlin.mff.cuni.cz/pub/local/mj/net/
Source0:	%{name}-%{version}.tar.gz
Patch0:		sleuth-1.3-relpath.patch
#Requires:	perl-Net-DNS
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildArch:	noarch

%description
Sleuth is a Perl script designed for easy checking of DNS zones
for common errors and also for processing of secondary name
service requests.

Sleuth also lists the corresponding RFC references with most of
its error messages, so that the people upset with their zones
being buggy can simply look up what exactly is going wrong and
how to fix it.

%prep

%setup -q -n %{name}-%{version}
%patch0 -p1

%build

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_sysconfdir}
install -d %{buildroot}%{_bindir}
install -d %{buildroot}/var/www/cgi-bin
install -m644 sleuth.conf %{buildroot}%{_sysconfdir}/
install -m755 sleuth %{buildroot}%{_bindir}/
install -m755 check.cgi %{buildroot}/var/www/cgi-bin/
install -m644 check.conf %{buildroot}/var/www/cgi-bin/

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog README THANKS TODO
%attr(0644,root,root) %config(noreplace,missingok) %{_sysconfdir}/sleuth.conf
%attr(0755,root,root) %{_bindir}/sleuth
%attr(0755,root,root) /var/www/cgi-bin/check.cgi
%attr(0644,root,root) /var/www/cgi-bin/check.conf



%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.4.3-5mdv2010.0
+ Revision: 433936
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.4.3-4mdv2009.0
+ Revision: 260794
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.4.3-3mdv2009.0
+ Revision: 252577
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Dec 16 2007 Anne Nicolas <anne.nicolas@mandriva.com> 1.4.3-1mdv2008.1
+ Revision: 120650
- New version

* Wed Aug 15 2007 Anne Nicolas <anne.nicolas@mandriva.com> 1.4-0.4mdv2008.0
+ Revision: 63549
- rebuild for 2008.0


* Fri Jul 14 2006 Oden Eriksson <oeriksson@mandriva.com> 1.4-0.3mdv2007.0
- rebuild

* Fri Jun 03 2005 Oden Eriksson <oeriksson@mandriva.com> 1.4-0.2mdk
- rebuild

* Sun May 16 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.4-0.1mdk
- 1.4-pre1

