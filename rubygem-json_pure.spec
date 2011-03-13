# Generated from json_pure-1.5.1.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	json_pure

Summary:	JSON Implementation for Ruby
Name:		rubygem-%{rbname}

Version:	1.5.1
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

%clean
rm -rf %{buildroot}

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/bin
%{ruby_gemdir}/gems/%{rbname}-%{version}/bin/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/data
%{ruby_gemdir}/gems/%{rbname}-%{version}/data/*.html
%{ruby_gemdir}/gems/%{rbname}-%{version}/data/*.js
%{ruby_gemdir}/gems/%{rbname}-%{version}/data/*.json
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/java
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/java/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/java/lib/*.jar
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/json
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/json/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/json/*.xpm
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/json/add
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/json/add/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/json/pure
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/json/pure/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/tools
%{ruby_gemdir}/gems/%{rbname}-%{version}/tools/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/README
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/tests
%{ruby_gemdir}/gems/%{rbname}-%{version}/tests/*
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/benchmarks
%{ruby_gemdir}/gems/%{rbname}-%{version}/benchmarks/*

%changelog
* Sun Mar 13 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.5.1-1
- Initial package
