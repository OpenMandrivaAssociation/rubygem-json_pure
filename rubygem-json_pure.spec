%define	rbname	json_pure

Summary:	JSON Implementation for Ruby
Name:		rubygem-%{rbname}

Version:	1.6.5
Release:	2
Group:		Development/Ruby
License:	GPLv2+
URL:		http://flori.github.com/json
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch

%description
This is an implementation of the JSON specification according to RFC 4627
(http://www.ietf.org/rfc/rfc4627.txt) written in pure ruby.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build -f '(benchmarks|data|java/lib|tests|tools)/'

%install
%gem_install
rm -rf %{buildroot}%{_bindir}

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/data
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/tools
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/json
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/json/add
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/json/pure
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/json/ext
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/json/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/tools/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/data/*.*
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/json/add/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/json/pure/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/json/ext/.keep
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/README.*
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/tests
%{ruby_gemdir}/gems/%{rbname}-%{version}/tests/*
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/benchmarks
%{ruby_gemdir}/gems/%{rbname}-%{version}/benchmarks/*


%changelog
* Wed Feb 15 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.6.5-2
+ Revision: 774161
- mass rebuild of ruby packages against ruby 1.9.1

* Mon Jan 23 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.6.5-1
+ Revision: 766957
- version update 1.6.5

  + Andrey Smirnov <asmirnov@mandriva.org>
    - rpmlint warning

* Sun Mar 13 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.5.1-2
+ Revision: 644356
- fix file conflicts with rubygem-json
- regenerate spec with gem2rpm5
- new release: 1.5.1

* Sun Dec 19 2010 Rémy Clouard <shikamaru@mandriva.org> 1.4.6-1mdv2011.0
+ Revision: 623081
- Bump release
- new version 1.4.6
- fix minor typo in %%description

* Thu Nov 04 2010 Rémy Clouard <shikamaru@mandriva.org> 1.2.4-1mdv2011.0
+ Revision: 593116
- bump release

* Fri Sep 17 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.2.0-2mdv2011.0
+ Revision: 579200
- rebuild for automatic provides

* Wed Feb 03 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.2.0-1mdv2010.1
+ Revision: 500331
- import rubygem-json_pure


* Mon Feb  3 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.2.0-1
- initial release
