# TODO
# - shared library?
Summary:	Fast Base64 encoding/decoding routines
Name:		libb64
Version:	1.2
Release:	1
License:	CC-PD
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libb64/%{name}-%{version}.src.zip
# Source0-md5:	a609809408327117e2c643bed91b76c5
URL:		http://libb64.sourceforge.net/
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fast Base64 encoding/decoding routines.

%package devel
Summary:	Header files for %{name} library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{name} library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki %{name}.

%prep
%setup -q

%build
# override -O3, -Werror non-sense
%{__make} -C src \
	CFLAGS="%{rpmcflags} -I../include"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}
cp -p src/libb64.a $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%files devel
%defattr(644,root,root,755)
%doc AUTHORS BENCHMARKS CHANGELOG README
%{_libdir}/libb64.a
