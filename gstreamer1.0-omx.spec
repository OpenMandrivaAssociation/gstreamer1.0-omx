%global optflags %{optflags} -O3

Name:           gstreamer1.0-omx
Version:        1.16.2
Release:        1
Summary:        GStreamer OpenMAX IL wrapper plugin
Group:          System/Libraries
License:        LGPLv2+
URL:            https://gstreamer.freedesktop.org/modules/gst-omx.html
Source0:        https://gstreamer.freedesktop.org/src/gst-omx/gst-omx-%{version}.tar.xz
BuildRequires:	pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:	pkgconfig(glesv2)
#BuildRequires:	pkgconfig(libomxil-bellagio)
%ifnarch %{riscv}
BuildRequires:	pkgconfig(valgrind)
%endif
Requires:	gstreamer1.0-plugins-base

%description
This plugin wraps available OpenMAX IL components and makes
them available as standard GStreamer elements.

%prep
%setup -qn gst-omx-%{version}
%autopatch -p1

%build
%configure \
	--with-omx-target=generic \
	--with-package-name='OpenMandriva %{name} package' \
	--with-package-origin='http://www.openmandriva.org/' \
%make_build V=1

%install
%make_install

# drop plugin docs
rm -rf %{buildroot}/%{_datadir}/gtk-doc/

# we don't want these
find %{buildroot} -name "*.la" -delete

%files
%doc NEWS README
%{_libdir}/gstreamer-1.0/libgstomx.so
