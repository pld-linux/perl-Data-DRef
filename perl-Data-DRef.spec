%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	Data-DRef perl module
Summary(pl):	Modu³ perla Data-DRef
Name:		perl-Data-DRef
Version:	1999.0206
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Data/Data-DRef-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
BuildRequires:	perl-String-Escape
%requires_eq	perl
Requires:	%{perl_sitearch}
Requires:	perl-String-Escape
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Data-DRef - Delimited-key access to complex data structures.

%description -l pl
Modu³ perla Data-DRef.

%prep
%setup -q -n Data-DRef-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Data/DRef
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%{perl_sitelib}/Data/DRef.pm
%{perl_sitearch}/auto/Data/DRef

%{_mandir}/man3/*
