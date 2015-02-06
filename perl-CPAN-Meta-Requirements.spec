%define upstream_name    CPAN-Meta-Requirements
%define upstream_version 2.125

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	A set of version requirements for a CPAN dist
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/CPAN/CPAN-Meta-Requirements-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(version)
BuildArch:	noarch

%description
A CPAN::Meta::Requirements object models a set of version constraints like
those specified in the _META.yml_ or _META.json_ files in CPAN
distributions. It can be built up by adding more and more constraints, and
it will reduce them to the simplest representation.

Logically impossible constraints will be identified immediately by thrown
exceptions.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc  META.json META.yml LICENSE Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*


