%define module  SVN-Notify
%define name    perl-%{module}
%define version 2.79
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Subversion activity notification
License:        GPL or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/SVN/%{module}-%{version}.tar.bz2
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(HTML::Parser)
BuildRequires:  sendmail-command
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
This class may be used for sending email messages for Subversion repository
activity. There are a number of different modes supported, and SVN::Notify is
fully subclassable, to easily add new functionality. By default, A list of all
the files affected by the commit will be assembled and listed in a single
message.

This package also provides a svnnotify command-line tool that can be directly
used in subversion post-commit scripts.

%prep
%setup -q -n %{module}-%{version}

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



