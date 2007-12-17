%define	version	0.83
%define release	%mkrel 7

Summary:	A board game similar to chess and go combined
Name:		gamazons
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Games/Boards
URL:		http://www.yorgalily.org/gamazons/
Source:		http://www.yorgalily.org/gamazons/src/%{name}-%{version}.tar.bz2
BuildRequires:	ImageMagick
BuildRequires:	libgnomeui2-devel

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

More info can be found at http://www.cs.ualberta.ca/~tegos/amazons/


%prep
%setup -q

%build
%configure2_5x --bindir=%{_gamesbindir}
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

mkdir -p %{buildroot}%{_menudir}
cat << _EOF_ > %{buildroot}%{_menudir}/%{name}
?package(%{name}): \
 command="%{_gamesbindir}/%{name}" \
 icon="gnome-gamazons.png" \
 longtitle="Amazons chess" \
 needs="x11" \
 section="More Applications/Games/Boards" \
 title="Gamazons" \
 xdg="true"
_EOF_

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-MoreApplications-Games-Boards;Game;BoardGame" \
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

%post
%{update_menus}

%postun
%{clean_menus}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc COPYING
%{_gamesbindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}
%{_datadir}/pixmaps/*
%{_menudir}/%{name}
%{_iconsdir}/gnome-gamazons.png
%{_miconsdir}/gnome-gamazons.png
%{_liconsdir}/gnome-gamazons.png

