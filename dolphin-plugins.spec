#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v27
# autospec commit: 65cf152
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : dolphin-plugins
Version  : 25.04.2
Release  : 82
URL      : https://download.kde.org/stable/release-service/25.04.2/src/dolphin-plugins-25.04.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/25.04.2/src/dolphin-plugins-25.04.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/25.04.2/src/dolphin-plugins-25.04.2.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
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
BuildRequires : gnupg
BuildRequires : kconfig-dev
BuildRequires : kcoreaddons-dev
BuildRequires : ki18n-dev
BuildRequires : kio-dev
BuildRequires : ktexteditor-dev
BuildRequires : qt6base-dev
BuildRequires : syntax-highlighting-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n dolphin-plugins-25.04.2
cd %{_builddir}/dolphin-plugins-25.04.2
pushd ..
cp -a dolphin-plugins-25.04.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1749504118
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1749504118
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/dolphin-plugins
cp %{_builddir}/dolphin-plugins-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/dolphin-plugins/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang mountisoaction
%find_lang fileviewbazaarplugin
%find_lang fileviewgitplugin
%find_lang fileviewhgplugin
%find_lang fileviewsvnplugin
%find_lang makefileactions
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/config.kcfg/fileviewgitpluginsettings.kcfg
/usr/share/config.kcfg/fileviewhgpluginsettings.kcfg
/usr/share/config.kcfg/fileviewsvnpluginsettings.kcfg
/usr/share/metainfo/org.kde.dolphin-plugins.metainfo.xml
/usr/share/qlogging-categories6/dolphingit.categories

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/qt6/plugins/dolphin/vcs/fileviewbazaarplugin.so
/V3/usr/lib64/qt6/plugins/dolphin/vcs/fileviewdropboxplugin.so
/V3/usr/lib64/qt6/plugins/dolphin/vcs/fileviewgitplugin.so
/V3/usr/lib64/qt6/plugins/dolphin/vcs/fileviewhgplugin.so
/V3/usr/lib64/qt6/plugins/dolphin/vcs/fileviewsvnplugin.so
/V3/usr/lib64/qt6/plugins/kf6/kfileitemaction/makefileactions.so
/V3/usr/lib64/qt6/plugins/kf6/kfileitemaction/mountisoaction.so
/usr/lib64/qt6/plugins/dolphin/vcs/fileviewbazaarplugin.so
/usr/lib64/qt6/plugins/dolphin/vcs/fileviewdropboxplugin.so
/usr/lib64/qt6/plugins/dolphin/vcs/fileviewgitplugin.so
/usr/lib64/qt6/plugins/dolphin/vcs/fileviewhgplugin.so
/usr/lib64/qt6/plugins/dolphin/vcs/fileviewsvnplugin.so
/usr/lib64/qt6/plugins/kf6/kfileitemaction/makefileactions.so
/usr/lib64/qt6/plugins/kf6/kfileitemaction/mountisoaction.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/dolphin-plugins/3e8971c6c5f16674958913a94a36b1ea7a00ac46

%files locales -f mountisoaction.lang -f fileviewbazaarplugin.lang -f fileviewgitplugin.lang -f fileviewhgplugin.lang -f fileviewsvnplugin.lang -f makefileactions.lang
%defattr(-,root,root,-)

