#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	WWW
%define	pnam	Poll
Summary:	WWW::Poll Perl module
Summary(cs):	Modul WWW::Poll pro Perl
Summary(da):	Perlmodul WWW::Poll
Summary(de):	WWW::Poll Perl Modul
Summary(es):	M�dulo de Perl WWW::Poll
Summary(fr):	Module Perl WWW::Poll
Summary(it):	Modulo di Perl WWW::Poll
Summary(ja):	WWW::Poll Perl �⥸�塼��
Summary(ko):	WWW::Poll �� ����
Summary(no):	Perlmodul WWW::Poll
Summary(pl):	Modu� Perla WWW::Poll
Summary(pt):	M�dulo de Perl WWW::Poll
Summary(pt_BR):	M�dulo Perl WWW::Poll
Summary(ru):	������ ��� Perl WWW::Poll
Summary(sv):	WWW::Poll Perlmodul
Summary(uk):	������ ��� Perl WWW::Poll
Summary(zh_CN):	WWW::Poll Perl ģ��
Name:		perl-WWW-Poll
Version:	0.01
Release:	10
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-undef.patch
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WWW::Poll - Perl extension to build web polls.

%description -l pl
WWW::Poll - modu� do tworzenia ankiet na stronach www.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p1

%build
%{__perl} Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

cp -ar demo/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/WWW/Poll.pm
# empty utosplit.ix
#%dir %{perl_sitelib}/auto/WWW/Poll
#%{perl_sitelib}/auto/WWW/Poll/autosplit.ix
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
