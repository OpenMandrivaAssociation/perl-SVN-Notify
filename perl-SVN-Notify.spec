%define upstream_name    SVN-Notify
%define upstream_version 2.84

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    2

Summary:    Subversion activity notification
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/SVN/SVN-Notify-%{upstream_version}.tar.gz

BuildRequires:  perl(Module::Build)
BuildRequires:  perl(HTML::Parser)
BuildRequires:  sendmail-command

BuildArch:      noarch

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
./Build install destdir=%{buildroot}

%files
%doc Changes
%{perl_vendorlib}/SVN
%{_mandir}/*/*
%{_bindir}/svnnotify


%changelog
* Sun Feb 20 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.810.0-1mdv2011.0
+ Revision: 638945
- update to new version 2.81

* Sat Jan 16 2010 Jérôme Quelin <jquelin@mandriva.org> 2.800.0-1mdv2011.0
+ Revision: 492162
- update to 2.80

* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 2.790.0-1mdv2010.0
+ Revision: 408048
- rebuild using %%perl_convert_version

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.79-1mdv2010.0
+ Revision: 370181
- update to new version 2.79

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.78-1mdv2009.1
+ Revision: 292350
- update to new version 2.78

* Sat Jul 19 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.77-1mdv2009.0
+ Revision: 238733
- update to new version 2.77

* Fri Jul 18 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.76-1mdv2009.0
+ Revision: 238039
- update to new version 2.76

* Tue May 20 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.75-1mdv2009.0
+ Revision: 209333
- update to new version 2.75

* Sat May 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.74-1mdv2009.0
+ Revision: 208375
- update to new version 2.74

* Tue May 06 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.73-1mdv2009.0
+ Revision: 201880
- update to new version 2.73

* Mon Apr 21 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.71-1mdv2009.0
+ Revision: 196169
- update to new version 2.71
- update to new version 2.71

* Sat Mar 01 2008 Michael Scherer <misc@mandriva.org> 2.70-1mdv2008.1
+ Revision: 177288
- update to new version 2.70

* Thu Feb 07 2008 Funda Wang <fwang@mandriva.org> 2.67-1mdv2008.1
+ Revision: 163388
- update to new version 2.67

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Jul 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.66-1mdv2008.0
+ Revision: 46689
- update to new version 2.66

* Wed May 02 2007 Olivier Thauvin <nanardon@mandriva.org> 2.65-1mdv2008.0
+ Revision: 20347
- 2.65


* Tue Nov 28 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.64-1mdv2007.0
+ Revision: 87819
- new version

* Tue Aug 08 2006 Olivier Thauvin <nanardon@mandriva.org> 2.63-2mdv2007.0
+ Revision: 54082
- rebuild
- Import perl-SVN-Notify

* Sat Aug 05 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.63-1mdv2007.0
- New version 2.63

* Sun Jul 02 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.62-1mdv2007.0
- New version 2.62

* Sat Jul 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.61-1mdv2007.0
- New version 2.61

* Thu Jun 22 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.60-1mdv2007.0
- New version 2.60

* Tue May 30 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.59-1mdv2007.0
- New release 2.59
- better source URL
- drop useless buildrequires

* Tue Apr 11 2006 Nicolas Lécureuil <neoclust@mandriva.org> 2.57-1mdk
- New release 2.57

* Thu Apr 06 2006 Nicolas Lécureuil <neoclust@mandriva.org> 2.56-1mdk
- New release 2.56

* Mon Mar 06 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.54-1mdk
- 2.54

* Fri Mar 03 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.53-1mdk
- 2.53

* Tue Jan 17 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.51-1mdk
- 2.51

* Tue Nov 29 2005 Guillaume Rousse <guillomovitch@mandriva.org> 2.50-1mdk
- new version
- rpmbuildupdate aware
- spec cleanup
- fix directory ownership

* Tue Oct 04 2005 Nicolas Lécureuil <neoclust@mandriva.org> 2.49-3mdk
- Fix BuildRequires

* Sat Oct 01 2005 Nicolas Lécureuil <neoclust@mandriva.org> 2.49-2mdk
- Buildrequires fix

* Sat Oct 01 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.49-1mdk
- Initial Mandriva release



