%define	version	0.83
%define release	%mkrel 9

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
BuildRequires:	libgnomeui2-devel
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

