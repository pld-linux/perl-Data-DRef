#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Data
%define		pnam	DRef
Summary:	Data::DRef - delimited-key access to complex data structures
Summary(pl):	Data::DRef - dostêp do z³o¿onych struktur danych w formie rozgraniczonej kluczami
Name:		perl-Data-DRef
Version:	1999.0206
Release:	10
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	de5d5b210ab97f95d1da483ba45584b9
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-String-Escape
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Data::DRef Perl module provides a streamlined interface for accessing
values within nested Perl data structures. These structures are
generally networks of hashes and arrays, some of which may be blessed
into various classes, containing a mix of simple scalar values and
references to other items in the structure.

%description -l pl
Modu³ Perla Data::DRef udostêpnia op³ywowy interfejs dostêpu do
warto¶ci w zagnie¿d¿onych strukturach danych Perla. Struktury te s± w
zasadzie sieciami hashy i tablic. Niektóre spo¶ród nich mog± byæ
przekszta³cone w ró¿ne klasy, zawieraj±ce mieszaninê prostych warto¶ci
skalarnych i odwo³añ do innych sk³adników struktury.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Data/DRef.pm
%{_mandir}/man3/*
