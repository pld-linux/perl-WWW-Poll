#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	WWW
%define	pnam	Poll
Summary:	WWW::Poll Perl module
Summary(cs):	Modul WWW::Poll pro Perl
Summary(da):	Perlmodul WWW::Poll
Summary(de):	WWW::Poll Perl Modul
Summary(es):	Módulo de Perl WWW::Poll
Summary(fr):	Module Perl WWW::Poll
Summary(it):	Modulo di Perl WWW::Poll
Summary(ja):	WWW::Poll Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	WWW::Poll ÆÞ ¸ðÁÙ
Summary(nb):	Perlmodul WWW::Poll
Summary(pl):	Modu³ Perla WWW::Poll
Summary(pt):	Módulo de Perl WWW::Poll
Summary(pt_BR):	Módulo Perl WWW::Poll
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl WWW::Poll
Summary(sv):	WWW::Poll Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl WWW::Poll
Summary(zh_CN):	WWW::Poll Perl Ä£¿é
Name:		perl-WWW-Poll
Version:	0.01
Release:	11
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9a67e34b5148440db0762ba7a66e5c0b
Patch0:		%{name}-undef.patch
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WWW::Poll - Perl extension to build web polls.

%description -l pl
WWW::Poll - modu³ do tworzenia ankiet na stronach www.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
cp -ar demo/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/WWW/Poll.pm
# empty utosplit.ix
#%dir %{perl_vendorlib}/auto/WWW/Poll
#%%{perl_vendorlib}/auto/WWW/Poll/autosplit.ix
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
