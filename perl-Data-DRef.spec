%include	/usr/lib/rpm/macros.perl
%define	pdir	Data
%define	pnam	DRef
Summary:	Data::DRef perl module
Summary(pl):	Modu³ perla Data::DRef
Name:		perl-Data-DRef
Version:	1999.0206
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	de5d5b210ab97f95d1da483ba45584b9
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-String-Escape
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Data::DRef - Delimited-key access to complex data structures.

%description -l pl
Modu³ perla Data::DRef.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Data/DRef.pm
%{_mandir}/man3/*
