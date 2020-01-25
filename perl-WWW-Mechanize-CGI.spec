#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	WWW
%define		pnam	Mechanize-CGI
Summary:	WWW::Mechanize::CGI - Use WWW::Mechanize with CGI applications
Name:		perl-WWW-Mechanize-CGI
Version:	0.3
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/WWW/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	67576d3b49654bce6657f0b3e5eb78d3
URL:		http://search.cpan.org/dist/WWW-Mechanize-CGI/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-HTTP-Request-AsCGI >= 0.2
BuildRequires:	perl-WWW-Mechanize
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides a convenient way of using CGI applications with
WWW::Mechanize.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/WWW/Mechanize/CGI.pm
%{_mandir}/man3/*
