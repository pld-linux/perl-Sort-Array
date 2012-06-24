%include	/usr/lib/rpm/macros.perl
%define		pdir	Sort
%define		pnam	Array
Summary:	Sort::Array Perl module
Summary(pl):	Modu� Perla Sort::Array
Name:		perl-Sort-Array
Version:	0.26
Release:	2
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9743023430bc3f5ccd8afc7ebd72d91a
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sort::Array - this extended sorting algorithm allows you to:
- sort an array by ANY field number, not only the first,
- find duplicates in your data-set and sort them out.

%description -l pl
Sort::Array - rozszerzony algorytm sortowania pozwalaj�cy na:
- sortowanie tablicy po dowolnym polu, nie koniecznie pierwszym,
- wyszukiwanie duplikat�w w zbiorze danych i odsortowywanie ich.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

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
