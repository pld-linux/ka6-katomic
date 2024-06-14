#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	24.05.1
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		katomic
Summary:	katomic
Name:		ka6-%{kaname}
Version:	24.05.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	6cf1882a36ba11f19eb04a51d055ca96
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel >= 5.11.1
BuildRequires:	Qt6Qml-devel >= 5.11.1
BuildRequires:	Qt6Quick-devel >= 5.11.1
BuildRequires:	Qt6Widgets-devel
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-devel
BuildRequires:	ka6-libkdegames-devel >= %{kdeappsver}
BuildRequires:	kf6-extra-cmake-modules >= %{kframever}
BuildRequires:	kf6-kconfig-devel >= %{kframever}
BuildRequires:	kf6-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf6-kcrash-devel >= %{kframever}
BuildRequires:	kf6-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf6-kdoctools-devel >= %{kframever}
BuildRequires:	kf6-ki18n-devel >= %{kframever}
BuildRequires:	kf6-knewstuff-devel >= %{kframever}
BuildRequires:	kf6-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf6-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Obsoletes:	ka5-%{kaname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KAtomic is a fun educational game built around molecular geometry. It
employs simplistic two-dimensional looks at different chemical
elements.

%description -l pl.UTF-8
KAtomic jest edukacyjną grą zbudowaną wokół geometrii cząsteczek
chemicznych. Pokazuje uproszczony dwuwymiarowy obraz różnych
chemicznych pierwiastków i związków.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/katomic
%{_desktopdir}/org.kde.katomic.desktop
%{_iconsdir}/hicolor/128x128/apps/katomic.png
%{_iconsdir}/hicolor/16x16/apps/katomic.png
%{_iconsdir}/hicolor/22x22/apps/katomic.png
%{_iconsdir}/hicolor/32x32/apps/katomic.png
%{_iconsdir}/hicolor/48x48/apps/katomic.png
%{_iconsdir}/hicolor/64x64/apps/katomic.png
%{_datadir}/katomic
##%attr(755,root,root) %{_datadir}/kconf_update/katomic-levelset-upd.pl
##%{_datadir}/kconf_update/katomic-levelset.upd
%{_datadir}/metainfo/org.kde.katomic.appdata.xml
%{_datadir}/knsrcfiles/katomic.knsrc
%{_datadir}/qlogging-categories6/katomic.categories
