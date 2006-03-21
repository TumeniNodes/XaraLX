Summary:	Xara Extreme LX Vector Image Editor
Summary(pl):	Edytor obrazów wektorowych Xara Extreme LX
Name:		XaraLX
Version:	0.3r693
Release:	1
License:	GPL with additional note - see LICENSE
Group:		X11/Applications
Source0:	http://downloads.xara.com/opensource/%{name}_%{version}.tar.bz2
# Source0-md5:	70c9490007e2d9914840f937ff28434d
Source1:	%{name}.desktop
URL:		http://www.xaraxtreme.org/
BuildRequires:	autoconf
BuildRequires:	automake
# ???
BuildRequires:	gettext-devel
BuildRequires:	libtool
BuildRequires:	perl-base
BuildRequires:	wxGTK2-unicode-devel >= 2.6.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xara eXtreme is a 2D vector graphics editor created by a small British
software company named Xara, notable for being the first vector
graphics software product to provide fully anti-aliased display,
advanced gradient fill and transparency tools, now available in many
of the competitors' products. Xara X is also notable for its usability
and very fast renderer

%description -l pl
Xara eXtreme jest edytorem grafiki 2D stworzonym przez ma³± brytyjsk±
firmê Xara, pierwszym wektorowym programem udostêpniaj±cym pe³ny
anty-aliasing, rozbudowane wype³nianie gradientami i narzêdzia do
prze¼roczysto¶ci, teraz dostêpne w wielu innych produktach. Xara X
jest tak¿e znana z u¿yteczno¶ci i prêdko¶ci dzia³ania.

%package examples
Summary:        Examples from Xara Extreme LX
Summary(pl):    Przyk³ady z Xara Extreme LX
Group:          X11/Applications

%description examples
Examples from Xara Extreme LX.

%description examples -l pl
Przyk³ady z Xara Extreme LX.

%prep
%setup -q

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-wx-config=wx-gtk2-unicode-config
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_examplesdir}/%{name},%{_desktopdir}}
cp -r Designs testfiles $RPM_BUILD_ROOT%{_examplesdir}/%{name}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}
