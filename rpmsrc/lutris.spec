%define debug_package %{nil}
Name:           lutris

Version:        0.5.8.1
Release:        2%{?dist}

Summary:        Install and play any video game easily

License:        GPLv3
URL:            http://%{name}.net
Source0:        %{URL}/releases/%{name}_%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  python3-devel
BuildRequires:  python3-gobject, python3-wheel, python3-setuptools, python3-gobject
Requires:       python3-evdev, python3-gobject, python3-PyYAML, cabextract
Requires:       gtk3, psmisc, xorg-x11-server-Xephyr, xrandr
Requires:       hicolor-icon-theme
Requires:       gnome-desktop3

%ifarch x86_64
Requires:       mesa-dri-drivers(x86-32)
Requires:       mesa-vulkan-drivers(x86-32)
Requires:       vulkan-loader(x86-32)
Requires:       mesa-libGL(x86-32)
%endif

Requires:       mesa-vulkan-drivers
Requires:       mesa-dri-drivers
Requires:       vulkan-loader
Requires:       mesa-libGL
Requires:       python3-requests
Requires:       python3-pillow
Requires:       glx-utils
Requires:       gvfs
Requires:       webkit2gtk3
Recommends:     wine-core
BuildRequires:  fdupes
BuildRequires:  libappstream-glib

#remove dependency on python-magic as it causes problems atm
# Patch0:         removing-python-magic-dep.patch
%description
Lutris is a gaming platform for GNU/Linux. Its goal is to make
gaming on Linux as easy as possible by taking care of installing
and setting up the game for the user. The only thing you have to
do is play the game. It aims to support every game that is playable
on Linux.

%prep
%autosetup -v -n %{name}-%{version} -p1


%build
%py3_build


%install
%py3_install
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/net.%{name}.Lutris.metainfo.xml

%fdupes %{buildroot}%{python3_sitelib}

desktop-file-install --dir=%{buildroot}%{_datadir}/applications share/applications/net.%{name}.Lutris.desktop

%files
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/net.%{name}.Lutris.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/22x22/apps/%{name}.png
%{_datadir}/icons/hicolor/24x24/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/man/man1/%{name}.1.gz
%{python3_sitelib}/%{name}-*.egg-info
%{python3_sitelib}/%{name}/
%{_datadir}/metainfo/

%changelog
* Sun Nov 29 2020 Christopher King <bunnyapocalypse@protonmail.com> - 0.5.8.1-2
- Patch to remove python-magic as a requirement to fix some issues

* Sun Nov 29 2020 Christopher King <bunnyapocalypse@protonmail.com> - 0.5.8.1-1
- New Version

* Wed Nov 18 2020 Christopher King <bunnyapocalypse@protonmail.com> - 0.5.8-1
- New Version

* Tue Jul 28 2020 Adam Jackson <ajax@redhat.com> - 0.5.7.1-3
- Require xrandr not xorg-x11-server-utils

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 2020 Christopher King <bunnyapocalypse@protonmail.com> - 0.5.7.1-1
- New Version

* Sun Jul 5 2020 Christopher King <bunnyapocalypse@protonmail.com> - 0.5.7-1
- New Version

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.6-2
- Rebuilt for Python 3.9

* Thu Apr 16 2020 Christopher King <bunnyapocalypse@protonmail.com> - 0.5.6-1
- New Version

* Sun Apr 05 2020 Christopher King <bunnyapocalypse@protonmail.com> - 0.5.5-2
- Removed unecessary comments 

* Sun Apr 05 2020 Christopher King <bunnyapocalypse@protonmail.com> - 0.5.5-1
- New Version

* Fri Mar 13 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.5.4-3
- Backport upstream patch. Fix #1806132

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 26 2020 Tomas Tomecek <ttomecek@redhat.com> - 0.5.4-1
- new upstream release: 0.5.4

* Sun Sep 8 2019 Christopher King <bunnyapocalypse@protonmail.com> - 0.5.3-1
- New Version

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.2.1-3
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 10 2019 Christopher King <bunnyapocalypse@protonmail.com> - 0.5.2.1-1
- New version

* Mon Apr 8 2019 Christopher King <bunnyapocalypse@protonmail.com> - 0.5.2-1
- New version

* Mon Feb 25 2019 Christopher King <bunnyapocalypse@protonmail.com> - 0.5.1.2-1
- New version

* Mon Feb 25 2019 Christopher King <bunnyapocalypse@protonmail.com> - 0.5.1.1-1
- New version

* Sun Feb 24 2019 Christopher King <bunnyapocalypse@protonmail.com> - 0.5.1-1
- New version

* Tue Feb 19 2019 Christopher King <bunnyapocalypse@protonmail.com> - 0.5.0.1-5
- More additional depends

* Sun Feb 3 2019 Christopher King <bunnyapocalypse@protonmail.com> - 0.5.0.1-2
- Forgot to add additional depends

* Sun Feb 3 2019 Christopher King <bunnyapocalypse@protonmail.com> - 0.5.0.1-1
- Updating version

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.23-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 3 2019 Christopher King <bunnyapocalypse@protonmail.com> - 0.4.23-8
- Forgot mesa-libGL drivers

* Sun Dec 30 2018 Christopher King <bunnyapocalypse@protonmail.com> - 0.4.23-7
- Forgot 64 bit mesa-dri drivers

* Sun Dec 30 2018 Christopher King <bunnyapocalypse@protonmail.com> - 0.4.23-6
- Changing depends again, specifying arches

* Fri Dec 28 2018 Christopher King <bunnyapocalypse@protonmail.com> - 0.4.23-5
- Changing the format of those previously added dependencies so that they work

* Thu Dec 20 2018 Christopher King <bunnyapocalypse@protonmail.com> - 0.4.23-4
- Adding some mesa depends to make Lutris work on more systems more reliably

* Fri Nov 16 2018 Christopher King <bunnyapocalypse@protonmail.com> - 0.4.23-3
- Turns out that I hadn't actually made a mistake, reverting most of the changes

* Thu Nov 15 2018 Christopher King <bunnyapocalypse@protonmail.com> - 0.4.23-2
- Updating this spec to actually install the appdata file

* Wed Nov 7 2018 Christopher King <bunnyapocalypse@protonmail.com> - 0.4.23
- New version

* Mon Nov 5 2018 Christopher King <bunnyapocalypse@protonmail.com> - 0.4.22
- New version

* Fri Nov 2 2018 Christopher King <bunnyapocalypse@protonmail.com> - 0.4.21.1
- New version

* Sat Oct 20 2018 Christopher King <bunnyapocalypse@protonmail.com> - 0.4.21
- New version

* Wed Oct 10 2018 Christopher King <bunnyapocalypse@protonmail.com> - 0.4.20
- Edit the SUSE build service spec file to be fedora specific

* Tue Nov 29 2016 Mathieu Comandon <strycore@gmail.com> - 0.4.3
- Ensure correct Python3 dependencies
- Set up Python macros for building (Thanks to Pharaoh_Atem on #opensuse-buildservice)

* Sat Oct 15 2016 Mathieu Comandon <strycore@gmail.com> - 0.4.0
- Update to Python 3
- Bump version to 0.4.0

* Sat Dec 12 2015 Rémi Verschelde <akien@mageia.org> - 0.3.7-2
- Remove ownership of system directories
- Spec file cleanup

* Fri Nov 27 2015 Mathieu Comandon <strycore@gmail.com> - 0.3.7-1
- Bump to version 0.3.7

* Thu Oct 30 2014 Mathieu Comandon <strycore@gmail.com> - 0.3.6-1
- Bump to version 0.3.6
- Add OpenSuse compatibility (contribution by @malkavi)

* Fri Sep 12 2014 Mathieu Comandon <strycore@gmail.com> - 0.3.5-1
- Bump version to 0.3.5

* Thu Aug 14 2014 Travis Nickles <nickles.travis@gmail.com> - 0.3.4-3
- Edited Requires to include pygobject3.

* Wed Jun 04 2014 Travis Nickles <nickles.travis@gmail.com> - 0.3.4-2
- Changed build and install step based on template generated by
  rpmdev-newspec.
- Added Requires.
- Ensure package can be built using mock.

* Tue Jun 03 2014 Travis Nickles <nickles.travis@gmail.com> - 0.3.4-1
- Initial version of the package
