%define upstream_name    Net-Redmine
%define upstream_version 0.08

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Represents a ticket
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Any::Moose)
BuildRequires: perl(DateTime::Format::DateParse)
BuildRequires: perl(DateTimeX::Easy)
BuildRequires: perl(Encode)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(HTML::WikiConverter)
BuildRequires: perl(HTML::WikiConverter::Markdown)
BuildRequires: perl(IO::All)
BuildRequires: perl(IO::String)
BuildRequires: perl(Params::Validate)
BuildRequires: perl(Quantum::Superpositions)
BuildRequires: perl(Test::Cukes)
BuildRequires: perl(Test::Memory::Cycle)
BuildRequires: perl(Test::More)
BuildRequires: perl(Text::CSV::Slurp)
BuildRequires: perl(Text::Greeking)
BuildRequires: perl(URI)
BuildRequires: perl(URI::Escape)
BuildRequires: perl(WWW::Mechanize)
BuildRequires: perl-pQuery
BuildRequires: perl(Regexp::Common)
BuildRequires: perl(Regexp::Common::Email::Address)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Net::Redmine is an mechanized-based programming API against redmine server.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


