#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Sort
%define		pnam	Array
Summary:	Sort::Array Perl module
Summary(pl.UTF-8):   Moduł Perla Sort::Array
Name:		perl-Sort-Array
Version:	0.26
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9743023430bc3f5ccd8afc7ebd72d91a
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sort::Array - this extended sorting algorithm allows you to:
- sort an array by ANY field number, not only the first,
- find duplicates in your data-set and sort them out.

%description -l pl.UTF-8
Sort::Array - rozszerzony algorytm sortowania pozwalający na:
- sortowanie tablicy po dowolnym polu, nie koniecznie pierwszym,
- wyszukiwanie duplikatów w zbiorze danych i odsortowywanie ich.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests: %{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Sort/Array.pm
%{_mandir}/man3/*
