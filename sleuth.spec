Summary:	Perl script for easy checking (DNS, common errors and etc.)
Name:		sleuth
Version:	1.4.3
Release:	%mkrel 1
License:	GPL
Group:		Networking/Other
URL:		ftp://atrey.karlin.mff.cuni.cz/pub/local/mj/net/
Source0:	%{name}-%{version}.tar.gz
Patch0:		sleuth-1.3-relpath.patch
#Requires:	perl-Net-DNS
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

