#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : dolphin-plugins
Version  : 20.08.3
Release  : 23
URL      : https://download.kde.org/stable/release-service/20.08.3/src/dolphin-plugins-20.08.3.tar.xz
Source0  : https://download.kde.org/stable/release-service/20.08.3/src/dolphin-plugins-20.08.3.tar.xz
Source1  : https://download.kde.org/stable/release-service/20.08.3/src/dolphin-plugins-20.08.3.tar.xz.sig
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
%setup -q -n dolphin-plugins-20.08.3
cd %{_builddir}/dolphin-plugins-20.08.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604592066
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1604592066
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/dolphin-plugins
cp %{_builddir}/dolphin-plugins-20.08.3/COPYING %{buildroot}/usr/share/package-licenses/dolphin-plugins/7c203dee3a03037da436df03c4b25b659c073976
pushd clr-build
%make_install
popd
%find_lang fileviewbazaarplugin
%find_lang fileviewgitplugin
%find_lang fileviewhgplugin
%find_lang fileviewsvnplugin
%find_lang mountisoaction

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/config.kcfg/fileviewgitpluginsettings.kcfg
/usr/share/config.kcfg/fileviewhgpluginsettings.kcfg
/usr/share/config.kcfg/fileviewsvnpluginsettings.kcfg
/usr/share/kservices5/fileviewbazaarplugin.desktop
/usr/share/kservices5/fileviewdropboxplugin.desktop
/usr/share/kservices5/fileviewgitplugin.desktop
/usr/share/kservices5/fileviewhgplugin.desktop
/usr/share/kservices5/fileviewsvnplugin.desktop
/usr/share/metainfo/org.kde.dolphin-plugins.metainfo.xml

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/fileviewbazaarplugin.so
/usr/lib64/qt5/plugins/fileviewdropboxplugin.so
/usr/lib64/qt5/plugins/fileviewgitplugin.so
/usr/lib64/qt5/plugins/fileviewhgplugin.so
/usr/lib64/qt5/plugins/fileviewsvnplugin.so
/usr/lib64/qt5/plugins/kf5/kfileitemaction/mountisoaction.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/dolphin-plugins/7c203dee3a03037da436df03c4b25b659c073976

%files locales -f fileviewbazaarplugin.lang -f fileviewgitplugin.lang -f fileviewhgplugin.lang -f fileviewsvnplugin.lang -f mountisoaction.lang
%defattr(-,root,root,-)

