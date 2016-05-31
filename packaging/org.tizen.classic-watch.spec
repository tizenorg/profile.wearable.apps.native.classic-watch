Name: org.tizen.classic-watch
Summary: classic-watch application (EFL)
Version: 0.0.1
Release: 0
Group: Applications/Wearable App
License: Flora-1.1
Source0: %{name}-%{version}.tar.gz
BuildRequires: pkgconfig(appcore-efl)
BuildRequires: pkgconfig(capi-appfw-watch-application)
BuildRequires: pkgconfig(capi-system-system-settings)
BuildRequires: pkgconfig(dlog)
BuildRequires: pkgconfig(elementary)
BuildRequires: pkgconfig(efl-extension)

BuildRequires: cmake
BuildRequires: edje-bin
BuildRequires: embryo-bin
BuildRequires: gettext-devel
BuildRequires: hash-signer

%ifarch %{arm}
%define ARCH arm
%else
%define ARCH emulator
%endif

%description
classic-watch.

%prep
%setup -q

%define PREFIX /usr/apps/org.tizen.classic-watch
%define DATADIR /usr/apps/%{name}/data

%build
%if 0%{?tizen_build_binary_release_type_eng}
export CFLAGS="$CFLAGS -DTIZEN_ENGINEER_MODE"
export CXXFLAGS="$CXXFLAGS -DTIZEN_ENGINEER_MODE"
export FFLAGS="$FFLAGS -DTIZEN_ENGINEER_MODE"
%endif

RPM_OPT=`echo $CFLAGS|sed 's/-Wp,-D_FORTIFY_SOURCE=2//'`
export CFLAGS=$RPM_OPT

cmake  -DCMAKE_INSTALL_PREFIX="%{PREFIX}" -DARCH="%{ARCH}" \
    -DENABLE_DIGITAL_OPERATOR_GEAR3=YES \

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%post
GOPTION="-g 5000 -f"
SOPTION="-s litewhome"

INHOUSE_ID="5000"
make_data_directory()
{
	I="%{DATADIR}"
	if [ ! -d $I ]; then
		mkdir -p $I
	fi
	chmod 775 $I
	chown :$INHOUSE_ID $I
}
make_data_directory

%files
%manifest org.tizen.classic-watch.manifest
%defattr(-,root,root,-)
%{PREFIX}/*
%{PREFIX}/bin/*
%{PREFIX}/res/*
/usr/share/packages/org.tizen.classic-watch.xml
/usr/apps/org.tizen.classic-watch/shared/res/org.tizen.classic-watch.png

