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
