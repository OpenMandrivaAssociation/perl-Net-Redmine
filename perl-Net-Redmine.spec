%define upstream_name    Net-Redmine
%define upstream_version 0.09

# for some old reason, perl(pQuery) is not provided
%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(pQuery\\)'
%else
%define _requires_exceptions perl\(pQuery\)
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.09
Release:	1

Summary:	Represents a ticket
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Net/Net-Redmine-0.09.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Any::Moose)
BuildRequires:	perl(DateTime::Format::DateParse)
BuildRequires:	perl(DateTimeX::Easy)
BuildRequires:	perl(Encode)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(HTML::WikiConverter)
BuildRequires:	perl(HTML::WikiConverter::Markdown)
BuildRequires:	perl(IO::All)
BuildRequires:	perl(IO::String)
BuildRequires:	perl(Params::Validate)
BuildRequires:	perl(Quantum::Superpositions)
BuildRequires:	perl(Test::Cukes)
BuildRequires:	perl(Test::Memory::Cycle)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Text::CSV::Slurp)
BuildRequires:	perl(Text::Greeking)
BuildRequires:	perl(URI)
BuildRequires:	perl(URI::Escape)
BuildRequires:	perl(Exporter::Lite)
BuildRequires:	perl(WWW::Mechanize)
BuildRequires:	perl-pQuery
BuildRequires:	perl(Regexp::Common)
BuildRequires:	perl(Regexp::Common::Email::Address)

Requires:	perl-pQuery

BuildArch: noarch

%description
Net::Redmine is an mechanized-based programming API against redmine server.

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
%doc Changes LICENSE META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.80.0-3mdv2011.0
+ Revision: 655429
- add br
- rebuild for updated spec-helper

* Fri May 07 2010 Michael Scherer <misc@mandriva.org> 0.80.0-2mdv2011.0
+ Revision: 543176
- fix installation, due to problem with lowercased perl modules

* Fri May 07 2010 Michael Scherer <misc@mandriva.org> 0.80.0-1mdv2010.1
+ Revision: 543169
- import perl-Net-Redmine


* Thu May 06 2010 cpan2dist 0.08-1mdv
- initial mdv release, generated with cpan2dist

