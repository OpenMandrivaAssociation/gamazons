%define	version	0.83
%define release	%mkrel 10

Summary:	A board game similar to chess and go combined
Name:		gamazons
Version:	%{version}
Release:	%{release}
License:	GPLv2
Group:		Games/Boards
URL:		http://www.yorgalily.org/gamazons/
Source:		http://www.yorgalily.org/gamazons/src/%{name}-%{version}.tar.bz2
Patch0:		gamazons-0.83-fix-desktop-file.patch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	imagemagick
BuildRequires:	pkgconfig(libgnomeui-2.0)
# (tv) for /usr/bin/desktop-file-install:
BuildRequires:	desktop-file-utils

%description
Amazons is a game played on a 10x10 chess board. Each side has four pieces
(amazons) that move like chess queens (in a straight line in any direction).
Instead of capturing pieces like in chess, the game is determined based on
who moves last.

Each move consists of two parts. First an amazon moves to a new square and
then fires an arrow to another square (the arrow is fired in a straight
line in any direction from the square the amazon landed on). The square
the arrow lands on becomes a permenant block for the rest of the game.
No one can move over it, or fire an arrow over it. Every turn an amazon
must move and fire an arrow, so every turn there is one less square
available on the board. Try and block in your opponent or section off a
good chunk of the board for yourself.


%prep
%setup -q
%patch0 -p1

%build
%configure2_5x --bindir=%{_gamesbindir}
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std


desktop-file-install --vendor="" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

mkdir -p $RPM_BUILD_ROOT%{_iconsdir} \
	 $RPM_BUILD_ROOT%{_miconsdir} \
	 $RPM_BUILD_ROOT%{_liconsdir}
install -m 0644         pixmaps/gnome-gamazons.png $RPM_BUILD_ROOT%{_liconsdir}/gnome-gamazons.png
convert -geometry 32x32 pixmaps/gnome-gamazons.png $RPM_BUILD_ROOT%{_iconsdir}/gnome-gamazons.png
convert -geometry 16x16 pixmaps/gnome-gamazons.png $RPM_BUILD_ROOT%{_miconsdir}/gnome-gamazons.png

# translation will come in future versions, find
# help files for now
%{find_lang} %{name} --with-gnome

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc COPYING
%{_gamesbindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}
%{_datadir}/pixmaps/*
%{_iconsdir}/gnome-gamazons.png
%{_miconsdir}/gnome-gamazons.png
%{_liconsdir}/gnome-gamazons.png



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.83-10mdv2011.0
+ Revision: 618395
- the mass rebuild of 2010.0 packages

* Thu May 14 2009 Samuel Verschelde <stormi@mandriva.org> 0.83-9mdv2010.0
+ Revision: 375632
- fix Licence
- fix desktop file (#49436)

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.83-8mdv2009.0
+ Revision: 222104
- BuildRequires desktop-file-utils for /usr/bin/desktop-file-install
- drop old menu
- kill re-definition of %%buildroot on Pixel's request
- import gamazons

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Thu Aug 10 2006 Lenny Cartier <lenny@mandriva.com> 0.83-7mdv2007.0
- xdg

* Fri Aug 05 2005 Abel Cheung <deaddog@mandriva.org> 0.83-6mdk
- rebuild

* Mon Nov 29 2004 Abel Cheung <deaddog@mandrake.org> 0.83-5mdk
- rebuild with correct gpg key
- move binary to gamesbindir

* Tue Sep 28 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.83-4mdk
- rebuild

* Sun Aug 17 2003 Abel Cheung <maddog@linux.org.hk> 0.83-3mdk
- Replace broken package and spec

* Tue Apr 29 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.83-2mdk
- buildrequires

* Mon Jan 06 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.83-1mdk
- from Arkadiusz Lipiec <alipiec@elka.pw.edu.pl> :
	- package created

