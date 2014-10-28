%define	rbname	json_pure

Summary:	JSON Implementation for Ruby
Name:		rubygem-%{rbname}

Version:	1.6.5
Release:	4
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
%dir %{gem_dir}/gems/%{rbname}-%{version}
%dir %{gem_dir}/gems/%{rbname}-%{version}/data
%dir %{gem_dir}/gems/%{rbname}-%{version}/tools
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib/json
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib/json/add
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib/json/pure
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib/json/ext
%{gem_dir}/gems/%{rbname}-%{version}/lib/json/*.rb
%{gem_dir}/gems/%{rbname}-%{version}/tools/*.rb
%{gem_dir}/gems/%{rbname}-%{version}/data/*.*
%{gem_dir}/gems/%{rbname}-%{version}/lib/*.rb
%{gem_dir}/gems/%{rbname}-%{version}/lib/json/add/*.rb
%{gem_dir}/gems/%{rbname}-%{version}/lib/json/pure/*.rb
%{gem_dir}/gems/%{rbname}-%{version}/lib/json/ext/.keep
%{gem_dir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%doc %{gem_dir}/gems/%{rbname}-%{version}/README.*
%doc %{gem_dir}/doc/%{rbname}-%{version}
%dir %{gem_dir}/gems/%{rbname}-%{version}/tests
%{gem_dir}/gems/%{rbname}-%{version}/tests/*
%dir %{gem_dir}/gems/%{rbname}-%{version}/benchmarks
%{gem_dir}/gems/%{rbname}-%{version}/benchmarks/*


