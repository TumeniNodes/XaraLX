#
Summary:	Xara Extreme LX Vector Image Editor
Name:		XaraLX
Version:	0.3r693
Release:	0.1
License:	- (enter GPL/GPL v2/LGPL/BSD/BSD-like/other license name here)
Group:		Applications
Source0:	http://downloads.xara.com/opensource/%{name}_%{version}.tar.bz2
# Source0-md5:	70c9490007e2d9914840f937ff28434d
URL:		http://www.xaraxtreme.org
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	perl
BuildRequires:	wxGTK2-unicode-devel > 2.6.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_bindir}/*
