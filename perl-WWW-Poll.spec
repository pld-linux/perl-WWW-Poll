%include	/usr/lib/rpm/macros.perl
%define	pdir	WWW
%define	pnam	Poll
Summary:	WWW-Poll perl module
Summary(pl):	Modu³ perla WWW-Poll
Name:		perl-WWW-Poll
Version:	0.01
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WWW-Poll - Perl extension to build web polls.

%description -l pl
WWW-Poll - modu³ do tworzenia ankiet na stronach www.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

cp -ar demo/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/WWW/Poll.pm
%{perl_sitelib}/auto/WWW/Poll/autosplit.ix
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
