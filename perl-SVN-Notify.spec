%define upstream_name    SVN-Notify
%define upstream_version 2.79

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Subversion activity notification
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/SVN/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:  perl(Module::Build)
BuildRequires:  perl(HTML::Parser)
BuildRequires:  sendmail-command
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
This class may be used for sending email messages for Subversion repository
activity. There are a number of different modes supported, and SVN::Notify is
fully subclassable, to easily add new functionality. By default, A list of all
the files affected by the commit will be assembled and listed in a single
message.

This package also provides a svnnotify command-line tool that can be directly
used in subversion post-commit scripts.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/SVN
%{_mandir}/*/*
%{_bindir}/svnnotify
