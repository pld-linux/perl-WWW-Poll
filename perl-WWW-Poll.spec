#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	WWW
%define		pnam	Poll
Summary:	WWW::Poll Perl module
Summary(cs.UTF-8):	Modul WWW::Poll pro Perl
Summary(da.UTF-8):	Perlmodul WWW::Poll
Summary(de.UTF-8):	WWW::Poll Perl Modul
Summary(es.UTF-8):	Módulo de Perl WWW::Poll
Summary(fr.UTF-8):	Module Perl WWW::Poll
Summary(it.UTF-8):	Modulo di Perl WWW::Poll
Summary(ja.UTF-8):	WWW::Poll Perl モジュール
Summary(ko.UTF-8):	WWW::Poll 펄 모줄
Summary(nb.UTF-8):	Perlmodul WWW::Poll
Summary(pl.UTF-8):	Moduł Perla WWW::Poll
Summary(pt.UTF-8):	Módulo de Perl WWW::Poll
Summary(pt_BR.UTF-8):	Módulo Perl WWW::Poll
Summary(ru.UTF-8):	Модуль для Perl WWW::Poll
Summary(sv.UTF-8):	WWW::Poll Perlmodul
Summary(uk.UTF-8):	Модуль для Perl WWW::Poll
Summary(zh_CN.UTF-8):	WWW::Poll Perl 模块
Name:		perl-WWW-Poll
Version:	0.01
Release:	13
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9a67e34b5148440db0762ba7a66e5c0b
URL:		http://search.cpan.org/dist/WWW-Poll/
Patch0:		%{name}-undef.patch
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WWW::Poll - Perl extension to build web polls.

%description -l pl.UTF-8
WWW::Poll - moduł do tworzenia ankiet na stronach WWW.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

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
cp -a demo/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

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
