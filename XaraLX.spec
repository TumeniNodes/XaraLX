Summary:	Xara Extreme LX Vector Image Editor
Summary(pl.UTF-8):	Edytor obrazów wektorowych Xara Extreme LX
Name:		XaraLX
Version:	0.7r1693
Release:	1
License:	GPL v2 with binary libraries - see LICENSE files
Group:		X11/Applications/Graphics
Source0:	http://downloads.xara.com/opensource/%{name}-%{version}.tar.bz2
# Source0-md5:	0cc4b17f918347a0dcb31cdbc2493155
Patch0:		%{name}-desktop.patch
URL:		http://www.xaraxtreme.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-autopoint
BuildRequires:	libtool
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	wxGTK2-unicode-devel >= 2.6.3
BuildRequires:	zip
ExclusiveArch:	%{ix86} %{x8664} ppc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xara eXtreme is a 2D vector graphics editor created by a small British
software company named Xara, notable for being the first vector
graphics software product to provide fully anti-aliased display,
advanced gradient fill and transparency tools, now available in many
of the competitors' products. Xara X is also notable for its usability
and very fast renderer

%description -l pl.UTF-8
Xara eXtreme jest edytorem grafiki 2D stworzonym przez małą brytyjską
firmę Xara, pierwszym wektorowym programem udostępniającym pełny
anty-aliasing, rozbudowane wypełnianie gradientami i narzędzia do
przeźroczystości, teraz dostępne w wielu innych produktach. Xara X
jest także znana z użyteczności i prędkości działania.

%package examples
Summary:	Examples from Xara Extreme LX
Summary(pl.UTF-8):	Przykłady z Xara Extreme LX
Group:		X11/Applications/Graphics

%description examples
Examples from Xara Extreme LX.

%description examples -l pl.UTF-8
Przykłady z Xara Extreme LX.

%prep
%setup -q
%patch0 -p1

%build
%{__autopoint}
%{__aclocal} -I m4
%{__libtoolize}
%{__autoconf}
%{__automake}
%configure \
	OPT_FLAGS="" \
	--with-wx-config=wx-gtk2-unicode-config
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_examplesdir}/%{name},%{_desktopdir},%{_pixmapsdir}}
cp -r Designs testfiles $RPM_BUILD_ROOT%{_examplesdir}/%{name}

ln -sf XaraLX $RPM_BUILD_ROOT%{_bindir}/xaralx

install xaralx.desktop $RPM_BUILD_ROOT%{_desktopdir}
install xaralx.png $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1 ||:

%postun
umask 022
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc LICENSE libs/LIBS-LICENSE
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}
