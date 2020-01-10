Summary:   Color management tools for GNOME
Name:      gnome-color-manager
Version:   3.14.2
Release:   1%{?dist}
License:   GPLv2+
Group:     Applications/System
URL:       http://mail.gnome.org/mailman/listinfo/gnome-color-manager-list
Source0:   http://download.gnome.org/sources/gnome-color-manager/3.14/%{name}-%{version}.tar.xz

# translation updates
Patch0: gnome-color-manager-translations-3.14.patch

Requires:  shared-mime-info

BuildRequires: gtk3-devel >= 3.0.0
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: intltool
BuildRequires: lcms2-devel
BuildRequires: libtiff-devel
BuildRequires: libexif-devel
BuildRequires: exiv2-devel
BuildRequires: libcanberra-devel
BuildRequires: glib2-devel >= 2.25.9-2
BuildRequires: docbook-utils
BuildRequires: colord-devel >= 0.1.12
BuildRequires: colord-gtk-devel >= 0.1.22
BuildRequires: itstool
BuildRequires: vte291-devel

# obsolete sub-package
Obsoletes: gnome-color-manager-devel <= 3.1.1
Provides: gnome-color-manager-devel

%description
gnome-color-manager is a session framework that makes it easy to manage, install
and generate color profiles in the GNOME desktop.

%prep
%setup -q
%patch0 -p1

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%find_lang %name --with-gnome

%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
update-desktop-database %{_datadir}/applications &> /dev/null || :

%postun
if [ $1 -eq 0 ]; then
    touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :
    gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
    glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi
update-desktop-database %{_datadir}/applications &> /dev/null || :

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING NEWS README
%{_bindir}/gcm-*
%{_libexecdir}/gcm-*
%{_datadir}/appdata/*.appdata.xml
%dir %{_datadir}/gnome-color-manager
%dir %{_datadir}/gnome-color-manager/targets
%dir %{_datadir}/gnome-color-manager/icons
%dir %{_datadir}/gnome-color-manager/figures
%dir %{_datadir}/gnome-color-manager/ti1
%{_datadir}/gnome-color-manager/targets/*
%{_datadir}/gnome-color-manager/icons/*
%{_datadir}/gnome-color-manager/figures/*
%{_datadir}/gnome-color-manager/ti1/*
%{_datadir}/man/man1/*.1.gz
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/scalable/*/*.svg*
%{_datadir}/applications/gcm-*.desktop

%changelog
* Mon Mar 23 2015 Richard Hughes <rhughes@redhat.com> - 3.14.2-1
- Update to 3.14.2
- Resolves: #1174571

* Thu Oct 31 2013 Richard Hughes <rhughes@redhat.com> - 3.8.2-3
- Do not build the clutter support to allow us to drop two deps
  now unsuitable for RHEL.
- Resolves: #1025270

* Wed Jul 10 2013 Matthias Clasen <mclasen@redhat.com> - 3.8.2-2
- Fix source url

* Mon May 13 2013 Richard Hughes <rhughes@redhat.com> - 3.8.2-1
- Update to 3.8.2

* Mon Apr 15 2013 Richard Hughes <rhughes@redhat.com> - 3.8.1-1
- Update to 3.8.1

* Tue Mar 26 2013 Richard Hughes <rhughes@redhat.com> - 3.8.0-1
- Update to 3.8.0

* Mon Mar 18 2013 Richard Hughes <rhughes@redhat.com> - 3.7.92-1
- Update to 3.7.92

* Thu Feb 21 2013 Kalev Lember <kalevlember@gmail.com> - 3.7.5-3
- Rebuilt for cogl soname bump

* Wed Feb 20 2013 Kalev Lember <kalevlember@gmail.com> - 3.7.5-2
- Rebuilt for libgnome-desktop soname bump

* Tue Feb 05 2013 Richard Hughes <rhughes@redhat.com> - 3.7.5-1
- Update to 3.7.5

* Fri Jan 25 2013 Peter Robinson <pbrobinson@fedoraproject.org> 3.6.1-2
- Rebuild for new cogl

* Thu Jan 10 2013 Richard Hughes <hughsient@gmail.com> - 3.6.1-1
- Update to 3.6.1

* Fri Dec 21 2012 Kalev Lember <kalevlember@gmail.com> - 3.6.0-3
- Rebuilt for libgnome-desktop-3 3.7.3 soname bump

* Tue Oct  2 2012 Matthias Clasen <mclasen@redhat.com> - 3.6.0-2
- Drop unnecessary GConf2 dep
- Update to 3.6.0

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 27 2012 Richard Hughes <hughsient@gmail.com> - 3.5.3-1
- Update to 3.5.3

* Fri Jun  8 2012 Matthias Clasen <mclasen@redhat.com> - 3.5.1-3
- Rebuild

* Mon May 28 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 3.5.1-2
- Add missing colord-gtk-devel, itstool dependencies

* Thu May 17 2012 Richard Hughes <hughsient@gmail.com> - 3.5.1-1
- Update to 3.5.1

* Wed May 02 2012 Rex Dieter <rdieter@fedoraproject.org> - 3.4.0-2
- rebuild (exiv2)

* Mon Mar 26 2012 Richard Hughes <rhughes@redhat.com> - 3.4.0-1
- New upstream version.

* Wed Mar 14 2012 Richard Hughes <rhughes@redhat.com> - 3.3.91-1
- New upstream version.

* Mon Feb 06 2012 Richard Hughes <rhughes@redhat.com> - 3.3.5-1
- New upstream version.

* Thu Jan 19 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.3-4
- Rebuild against new cogl

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 19 2011 Richard Hughes <rhughes@redhat.com> - 3.3.3-2
- Add BR gnome-desktop3-devel

* Mon Dec 19 2011 Richard Hughes <rhughes@redhat.com> - 3.3.3-1
- New upstream version.

* Thu Nov 24 2011 Matthias Clasen <mclasen@redhat.com> - 3.2.1-2
- Rebuild against new clutter

* Mon Oct 17 2011 Richard Hughes <rhughes@redhat.com> - 3.2.1-1
- New upstream version.

* Fri Oct 14 2011 Rex Dieter <rdieter@fedoraproject.org> - 3.2.0-4
- rebuild (exiv2)

* Thu Oct 06 2011 Adam Jackson <ajax@redhat.com> 3.2.0-3
- 0001-Initialize-error-pointer-for-gdk_pixbuf_new_from_fil.patch: Backport
  a crash fix from mainline.

* Mon Sep 26 2011 Richard Hughes <rhughes@redhat.com> - 3.2.0-2
- Rebuild for libmash API update.

* Mon Sep 26 2011 Richard Hughes <rhughes@redhat.com> - 3.2.0-1
- New upstream version.

* Mon Sep 19 2011 Richard Hughes <rhughes@redhat.com> - 3.1.92-1
- New upstream version.

* Fri Sep 16 2011 Richard Hughes <rhughes@redhat.com> - 3.1.91-3
- Rebuild for libmash soname update (which for the moment will disable
  the 3D renderer code).

* Mon Sep 05 2011 Richard Hughes <rhughes@redhat.com> - 3.1.91-1
- New upstream version.

* Tue Aug 30 2011 Richard Hughes <rhughes@redhat.com> - 3.1.90-2
- BR a high enough colord.

* Tue Aug 30 2011 Richard Hughes <rhughes@redhat.com> - 3.1.90-1
- New upstream version.

* Mon Jun 13 2011 Richard Hughes <rhughes@redhat.com> - 3.1.2-1
- New upstream version.

* Sat May 07 2011 Christopher Aillon <caillon@redhat.com> - 3.1.1-2
- Update gsettings scriptlet

* Fri May 06 2011 Richard Hughes <rhughes@redhat.com> - 3.1.1-1
- New upstream version.

* Mon Apr 04 2011 Richard Hughes <rhughes@redhat.com> - 3.0.0-1
- New upstream version.

* Mon Mar 21 2011 Richard Hughes <rhughes@redhat.com> - 2.91.92-3
- No gtk-doc anymore.

* Mon Mar 21 2011 Richard Hughes <rhughes@redhat.com> - 2.91.92-2
- We're installing into gnome-settings-daemon-3.0 now.

* Mon Mar 21 2011 Richard Hughes <rhughes@redhat.com> - 2.91.92-1
- New upstream version.

* Thu Feb 20 2011 Matthias Clasen <mclasen@redhat.com> 2.91.5-4
- Rebuild against newer gtk

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.91.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb  2 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.5-2
- Rebuild against newer gtk

* Tue Jan 11 2011 Richard Hughes <rhughes@redhat.com> - 2.91.5-1
- New upstream version.

* Sun Jan  9 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.3-4
- Rebuild against newer gtk3

* Sat Jan 01 2011 Rex Dieter <rdieter@fedoraproject.org> - 2.91.3-3
- rebuild (exiv2)

* Fri Dec 03 2010 Peter Robinson <pbrobinson@gmail.com> 2.91.3-2
- Move devel files to sub package, cleanup spec file

* Wed Dec 01 2010 Richard Hughes <richard@hughsie.com> 2.91.3-1
- New upstream release.

* Mon Nov 08 2010 Richard Hughes <richard@hughsie.com> 2.91.2-1
- New upstream release.

* Wed Nov 03 2010 Richard Hughes <richard@hughsie.com> 2.91.2-0.3.20101102
- Rebuild now libnotify 0.7.0 is in rawhide, actually.

* Wed Nov 03 2010 Richard Hughes <richard@hughsie.com> 2.91.2-0.2.20101102
- Rebuild now libnotify 0.7.0 is in rawhide.

* Tue Nov 02 2010 Richard Hughes <richard@hughsie.com> 2.91.2-0.1.20101102
- Update to a git snapshot to fix rawhide.

* Tue Oct 05 2010 Richard Hughes <richard@hughsie.com> 2.91.1-4
- Add BR docbook-utils

* Tue Oct 05 2010 Richard Hughes <richard@hughsie.com> 2.91.1-3
- Add BR libusb1-devel

* Tue Oct 05 2010 Richard Hughes <richard@hughsie.com> 2.91.1-2
- Add BR gnome-settings-daemon-devel

* Tue Oct 05 2010 Richard Hughes <richard@hughsie.com> 2.91.1-1
- New upstream release.

* Mon Sep 11 2010 Richard Hughes <richard@hughsie.com> 2.31.4-2
- Remove the explicit dependency on yelp.
- Resolves: #626242

* Thu Jul 01 2010 Richard Hughes <richard@hughsie.com> 2.31.4-1
- New upstream release.

* Mon Jun 28 2010 Matthias Clasen <mclasen@redhat.com> 2.31.3-3
- Rebuild

* Tue Jun 22 2010 Richard Hughes <richard@hughsie.com> 2.31.3-2
- Actually upload new tarball. Grrr.

* Mon Jun 21 2010 Richard Hughes <richard@hughsie.com> 2.31.3-1
- New upstream release.

* Wed Jun 16 2010 Matthias Clasen <mclasen@redhat.com> 2.31.2-5
- Nuke the scrollkeeper runtime dep

* Thu Jun 03 2010 Richard Hughes <richard@hughsie.com> 2.31.2-4
- Patience is a virtue, pursue it if you can -- never in a programmer
  always in a can.

* Wed Jun 02 2010 Richard Hughes <richard@hughsie.com> 2.31.2-3
- Build against the fixed sane-backends.

* Wed Jun 02 2010 Richard Hughes <richard@hughsie.com> 2.31.2-2
- Actually upload source tarball...

* Wed Jun 02 2010 Richard Hughes <richard@hughsie.com> 2.31.2-1
- New upstream release.

* Thu May 06 2010 Richard Hughes <richard@hughsie.com> 2.31.1-1
- New upstream release.

* Mon Apr 26 2010 Matthias Clasen <mclasen@redhat.com> 2.30.1-1
- Update to 2.30.1

* Fri Apr  2 2010 Matthias Clasen <mclasen@redhat.com> 2.30.0-4
- BR GConf to make the macros work
- Modernize icon cache handling

* Wed Mar 31 2010 Richard Hughes <richard@hughsie.com> 2.30.0-3
- Fix up a scriptlet problem.
- Resolves: #578611

* Mon Mar 29 2010 Richard Hughes <richard@hughsie.com> 2.30.0-2
- Add libnotify BR.

* Mon Mar 29 2010 Richard Hughes <richard@hughsie.com> 2.30.0-1
- New upstream release.

* Tue Mar 09 2010 Richard Hughes <richard@hughsie.com> 2.29.4-2
- Update to the latest version of the Fedora Packaging Guidelines
- Remove the custom BuildRoot
- Do not clean the buildroot before install
- Use the gconf_schema defines for the GConf schemas
- Remove some over-zealous Requires that are already picked up by rpm.
- Resolves #571658

* Mon Mar 01 2010 Richard Hughes <richard@hughsie.com> 2.29.4-1
- New upstream release.

* Mon Feb 22 2010 Richard Hughes <richard@hughsie.com> 2.29.4-0.1.20100222
- Another new snapshot from upstream with lots of bugs fixed from the Fedora
  test day.

* Wed Feb 18 2010 Richard Hughes <richard@hughsie.com> 2.29.4-0.1.20100218
- Another new snapshot from upstream for the Fedora test day.

* Wed Feb 17 2010 Richard Hughes <richard@hughsie.com> 2.29.4-0.1.20100217
- New snapshot from upstream for the Fedora test day.

* Mon Feb 01 2010 Richard Hughes <richard@hughsie.com> 2.29.3-1
- New upstream release.

* Mon Jan 18 2010 Matthias Clasen <mclasen@redhat.com> 2.29.2-3
- Rebuild against new gnome-desktop

* Mon Jan 04 2010 Richard Hughes <richard@hughsie.com> 2.29.2-2
- Rebuild, hopefully koji has now a working glibc.

* Mon Jan 04 2010 Richard Hughes <richard@hughsie.com> 2.29.2-1
- New upstream release.

* Fri Dec 04 2009 Richard Hughes <richard@hughsie.com> 2.29.1-1
- Initial spec for review.

