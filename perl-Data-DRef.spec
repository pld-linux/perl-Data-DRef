%include	/usr/lib/rpm/macros.perl
Summary:	Data-DRef perl module
Summary(pl):	Modu³ perla Data-DRef
Name:		perl-Data-DRef
Version:	1999.0206
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Data/Data-DRef-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-String-Escape
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Data-DRef - Delimited-key access to complex data structures.

%description -l pl
Modu³ perla Data-DRef.

%prep
%setup -q -n Data-DRef-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/Data/DRef.pm
%{_mandir}/man3/*
