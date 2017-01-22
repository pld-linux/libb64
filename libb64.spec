Summary:	Fast Base64 encoding/decoding routines
Summary(pl.UTF-8):	Szybkie funkcje do kodowania/dekodowania Base64
Name:		libb64
Version:	1.2.1
Release:	1
License:	CC-PD
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libb64/%{name}-%{version}.zip
# Source0-md5:	8a5dc72eb7e32f074605260bc127c764
URL:		http://libb64.sourceforge.net/
BuildRequires:	libtool >= 2:1.5
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fast Base64 encoding/decoding routines.

%description -l pl.UTF-8
Szybkie funkcje do kodowania/dekodowania Base64.

%package devel
Summary:	Header files for b64 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki b64
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for b64 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki b64.

%package static
Summary:	Static b64 library
Summary(pl.UTF-8):	Statyczna biblioteka b64
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static b64 library.

%description static -l pl.UTF-8
Statyczna biblioteka b64.

%prep
%setup -q

%build
cd src
for f in cencode.c cdecode.c ; do
	libtool --mode=compile %{__cc} %{rpmcflags} %{rpmcppflags} -c $f -o ${f%.c}.lo -I../include
done
libtool --mode=link %{__cc} %{rpmldflags} %{rpmcflags} -o libb64.la cencode.lo cdecode.lo -rpath %{_libdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

cd src
libtool --mode=install install libb64.la $RPM_BUILD_ROOT%{_libdir}
cd ..
cp -pr include/b64 $RPM_BUILD_ROOT%{_includedir}

# no external dependencies
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libb64.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS BENCHMARKS CHANGELOG LICENSE README
%attr(755,root,root) %{_libdir}/libb64.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libb64.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libb64.so
%{_includedir}/b64

%files static
%defattr(644,root,root,755)
%{_libdir}/libb64.a
