Summary:	X.org video driver for Sun CG14 video cards
Summary(pl):	Sterownik obrazu X.org dla kart graficznych Sun CG14
Name:		xorg-driver-video-suncg14
Version:	1.0.0.2
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC2/driver/xf86-video-suncg14-%{version}.tar.bz2
# Source0-md5:	994084d7a5b2f1750fe81ab1f06b7806
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.1
BuildRequires:	xorg-xserver-server-devel >= 0.99.3
ExclusiveArch:	sparc sparcv9 sparc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for Sun CG14 video cards.

%description -l pl
Sterownik obrazu X.org dla kart graficznych Sun CG14.

%prep
%setup -q -n xf86-video-suncg14-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	drivermandir=%{_mandir}/man4

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/suncg14_drv.so
%{_mandir}/man4/suncg14.4x*
