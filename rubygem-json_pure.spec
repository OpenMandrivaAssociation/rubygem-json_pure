%define	oname	json_pure

Summary:	A JSON implementation in pure Ruby
Name:		rubygem-%{oname}
Version:	1.2.4
Release:	%mkrel 1
License:	GPLv2
Group:		Development/Ruby
URL:		http://%{oname}.rubyforge.org/
Source0:	http://gems.rubyforge.org/gems/%{oname}-%{version}.gem
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	ruby-RubyGems
Requires:	ruby
BuildArch:	noarch

%description
This is a implementation of the JSON specification according to RFC 4627
(http://www.ietf.org/rfc/rfc4627.txt) written in pure ruby.

%prep

%build

%install
rm -rf %{buildroot}
gem install --local --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}

chmod g-w,g+r,o+r -R %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%{ruby_gemdir}/bin/*_json.rb
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/gems/%{oname}-%{version}
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec

