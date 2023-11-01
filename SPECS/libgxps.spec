Name:           libgxps
Version:        0.3.0
Release:        5%{?dist}
Summary:        GObject based library for handling and rendering XPS documents

License:        LGPLv2+
URL:            https://wiki.gnome.org/Projects/libgxps
Source0:        https://ftp.gnome.org/pub/gnome/sources/%{name}/0.3/%{name}-%{version}.tar.xz

# https://bugzilla.redhat.com/show_bug.cgi?id=1576113
Patch0:         libgxps-0.3.0-archive-fill-error.patch
Patch1:         libgxps-0.3.0-archive-handle-error.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1524378
Patch2:         libgxps-0.3.0-integer-overflow.patch
Patch3:         libgxps-0.3.0-clear-error.patch

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  gtk3-devel
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  cairo-devel
BuildRequires:  libarchive-devel
BuildRequires:  freetype-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  lcms2-devel

%description
libgxps is a GObject based library for handling and rendering XPS
documents.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        tools
Summary:        Command-line utility programs for manipulating XPS files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    tools
The %{name}-tools contains command-line programs for manipulating XPS format
documents using the %{name} library.


%prep
%autosetup -p1


%build
%meson -Denable-gtk-doc=true -Denable-man=true
%meson_build


%install
%meson_install


%files
%doc AUTHORS MAINTAINERS NEWS README TODO
%license COPYING
%{_libdir}/*.so.*
%{_libdir}/girepository-1.0/*.typelib


%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/*.gir
%{_datadir}/gtk-doc/html/libgxps


%files tools
%{_bindir}/xpsto*
%{_mandir}/man1/xpsto*.1.gz


%changelog
* Thu Jun 21 2018 Marek Kasik <mkasik@redhat.com> - 0.3.0-5
- Fix integer overflow in png decoder
- Clear the error before trying to load an image again
- Resolves: #1524378

* Wed Jun 20 2018 Marek Kasik <mkasik@redhat.com> - 0.3.0-4
- Ensure gxps_archive_read_entry() fills the GError in case of failure
- Handle errors returned by archive_read_data()
- Fixes CVE-2018-10733
- Resolves: #1576113

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Tom Hughes <tom@compton.nu> - 0.3.0-2
- Drop ldconfig scriptlets

* Thu Aug 10 2017 Tom Hughes <tom@compton.nu> - 0.3.0-1
- Update to 0.3.0 upstream release

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 25 2017 Tom Hughes <tom@compton.nu> - 0.2.5-1
- Update to 0.2.5 upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jun 21 2016 Tom Hughes <tom@compton.nu> - 0.2.4-1
- Update to 0.2.4 upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep  4 2015 Tom Hughes <tom@compton.nu> - 0.2.3.2-1
- Update to 0.2.3.2 upstream release

* Sat Aug 15 2015 Tom Hughes <tom@compton.nu> - 0.2.3.1-1
- Update to 0.2.3.1 upstream release

* Thu Aug 13 2015 Tom Hughes <tom@compton.nu> - 0.2.3-1
- Update to 0.2.3 upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 0.2.2-10
- Rebuilt for gobject-introspection 1.41.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 0.2.2-6
- rebuild due to "jpeg8-ABI" feature drop

* Thu Jan 17 2013 Tomas Bzatek <tbzatek@redhat.com> - 0.2.2-5
- Rebuilt for new libarchive

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 0.2.2-4
- rebuild against new libjpeg

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun May  6 2012 Tom Hughes <tom@compton.nu> - 0.2.2-2
- Rebuilt for new libtiff.

* Mon Mar 19 2012 Tom Hughes <tom@compton.nu> - 0.2.2-1
- Update to 0.2.2 upstream release.

* Thu Jan 26 2012 Tomas Bzatek <tbzatek@redhat.com> - 0.2.1-4
- Rebuilt for new libarchive

* Thu Jan 26 2012 Tom Hughes <tom@compton.nu> - 0.2.1-3
- Correct summary and description for tools package.

* Thu Jan 26 2012 Tom Hughes <tom@compton.nu> - 0.2.1-2
- Rebuild for libarchive soname bump.

* Sat Jan 21 2012 Tom Hughes <tom@compton.nu> - 0.2.1-1
- Update to 0.2.1 upstream release.

* Wed Jan  4 2012 Tom Hughes <tom@compton.nu> - 0.2.0-2
- Rebuilt for gcc 4.7 mass rebuild.
- Run autoreconf to update libtool.

* Thu Dec  1 2011 Tom Hughes <tom@compton.nu> - 0.2.0-1
- Update to 0.2.0 upstream release.

* Sat Nov  5 2011 Tom Hughes <tom@compton.nu> - 0.1.0-2
- Fix base package dependency in devel package.

* Fri Nov  4 2011 Tom Hughes <tom@compton.nu> - 0.1.0-1
- Initial build.
