%include	/usr/lib/rpm/macros.perl
Summary:	WWW-Poll perl module
Summary(pl):	Modu³ perla WWW-Poll
Name:		perl-WWW-Poll
Version:	0.01
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/WWW/WWW-Poll-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
WWW-Poll - Perl extension to build web polls. 

%description -l pl
WWW-Poll - modu³ do tworzenia ankiet na stronach www.

%prep
%setup -q -n WWW-Poll-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/src/examples/%{name}-%{version}

make install DESTDIR=$RPM_BUILD_ROOT

cp -ar demo/* $RPM_BUILD_ROOT/usr/src/examples/%{name}-%{version}

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/WWW/Poll
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitelib}/WWW/Poll.pm
%{perl_sitelib}/auto/WWW/Poll/autosplit.ix
%{perl_sitearch}/auto/WWW/Poll

%{_mandir}/man3/*

/usr/src/examples/%{name}-%{version}
