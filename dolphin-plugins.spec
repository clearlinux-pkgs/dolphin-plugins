#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : dolphin-plugins
Version  : 21.12.2
Release  : 35
URL      : https://download.kde.org/stable/release-service/21.12.2/src/dolphin-plugins-21.12.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/21.12.2/src/dolphin-plugins-21.12.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/21.12.2/src/dolphin-plugins-21.12.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: dolphin-plugins-data = %{version}-%{release}
Requires: dolphin-plugins-lib = %{version}-%{release}
Requires: dolphin-plugins-license = %{version}-%{release}
Requires: dolphin-plugins-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : dolphin-dev
BuildRequires : extra-cmake-modules-data
BuildRequires : ktexteditor-dev
BuildRequires : syntax-highlighting-dev

%description
No detailed description available

%package data
Summary: data components for the dolphin-plugins package.
Group: Data

%description data
data components for the dolphin-plugins package.


%package lib
Summary: lib components for the dolphin-plugins package.
Group: Libraries
Requires: dolphin-plugins-data = %{version}-%{release}
Requires: dolphin-plugins-license = %{version}-%{release}

%description lib
lib components for the dolphin-plugins package.


%package license
Summary: license components for the dolphin-plugins package.
Group: Default

%description license
license components for the dolphin-plugins package.


%package locales
Summary: locales components for the dolphin-plugins package.
Group: Default

%description locales
locales components for the dolphin-plugins package.


%prep
%setup -q -n dolphin-plugins-21.12.2
cd %{_builddir}/dolphin-plugins-21.12.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1644104032
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1644104032
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/dolphin-plugins
cp %{_builddir}/dolphin-plugins-21.12.2/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/dolphin-plugins/3e8971c6c5f16674958913a94a36b1ea7a00ac46
pushd clr-build
%make_install
popd
%find_lang mountisoaction
%find_lang fileviewbazaarplugin
%find_lang fileviewgitplugin
%find_lang fileviewhgplugin
%find_lang fileviewsvnplugin

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/config.kcfg/fileviewgitpluginsettings.kcfg
/usr/share/config.kcfg/fileviewhgpluginsettings.kcfg
/usr/share/config.kcfg/fileviewsvnpluginsettings.kcfg
/usr/share/metainfo/org.kde.dolphin-plugins.metainfo.xml

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/dolphin/vcs/fileviewbazaarplugin.so
/usr/lib64/qt5/plugins/dolphin/vcs/fileviewdropboxplugin.so
/usr/lib64/qt5/plugins/dolphin/vcs/fileviewgitplugin.so
/usr/lib64/qt5/plugins/dolphin/vcs/fileviewhgplugin.so
/usr/lib64/qt5/plugins/dolphin/vcs/fileviewsvnplugin.so
/usr/lib64/qt5/plugins/kf5/kfileitemaction/mountisoaction.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/dolphin-plugins/3e8971c6c5f16674958913a94a36b1ea7a00ac46

%files locales -f mountisoaction.lang -f fileviewbazaarplugin.lang -f fileviewgitplugin.lang -f fileviewhgplugin.lang -f fileviewsvnplugin.lang
%defattr(-,root,root,-)

