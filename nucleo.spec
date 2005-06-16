Summary:	A toolking for exploring new uses of video
Summary(pl):	Narzędzie do odkrywania nowych zastosowań grafiki
Name:		nucleo
%define	_tardate	2005-06-03
%define	_snap	%(echo %{_tardate} | sed s/-//g)
#%%define		_snap	20041216
Version:	0.1
Release:	0.%{_snap}.1
License:	LGPL v2.1
Group:		X11
Source0:	http://insitu.lri.fr/~roussel/software/src/%{name}-%{_tardate}.tar.bz2
# Source0-md5:	59c7153eb269d6ab5325b54763d567f8
#Source0:	http://insitu.lri.fr/~chapuis/software/metisse/%{name}-%{version}-%{_snap}.tar.bz2
Patch0:		%{name}-nv.patch
URL:		http://insitu.lri.fr/~roussel/projects/nucleo/
BuildRequires:	XFree86-OpenGL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nucleo is a toolking for exploring new uses of video and new
human-computer interaction techniques. Most of it comes from a
previous toolkit named videoSpace.

%description -l pl
Nucleo to narzędzie do odkrywania nowych zastosowań grafiki oraz
technik interakcji człowiek - komputer. Większość zaczerpnięta
została z toolkitu videoSpace.

%package devel
Summary:	Header files for nucleo
Summary(pl):	Pliki nagłówkowe dla nucleo
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for nucleo.

%description devel -l pl
Pliki nagłówkowe dla nucleo.

%prep
%setup -q -n %{name}-%{_tardate}
#%%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
#some script for MacOS
rm $RPM_BUILD_ROOT%{_bindir}/nBundle 

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/[!n]*
%attr(755,root,root) %{_bindir}/nTest
%attr(755,root,root) %{_libdir}/libNucleo.so.*.*
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/nucleo-config
%attr(755,root,root) %{_libdir}/libNucleo.so
%{_libdir}/libNucleo.la
%{_includedir}/%{name}
%{_pkgconfigdir}/%{name}.pc
