Summary:	A collection of LADSPA plugins from Computer Music Toolkit
Summary(pl.UTF-8):	Kolekcja wtyczek LADSPA z projektu Computer Music Toolkit
Name:		ladspa-cmt-plugins
Version:	1.18
Release:	1
License:	GPL v2+
Group:		Applications/Sound
Source0:	http://www.ladspa.org/download/cmt_%{version}.tgz
# Source0-md5:	c81b266dd83c2f9be729795760422b0b
Patch0:		%{name}-makefile.patch
Patch1:		%{name}-compile.patch
URL:		http://www.ladspa.org/
BuildRequires:	ladspa-devel
BuildRequires:	libstdc++-devel
Requires:	ladspa-common
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Computer Music Toolkit (CMT) is a collection of LADSPA plugins for
use with software synthesis and recording packages on Linux.

%description -l pl.UTF-8
Computer Music Toolkit jest kolekcją wtyczek LADSPA do użytku z
syntezatorami programowymi i programami nagrywającymi dźwięk pod
Linuksem.

%prep
%setup -q -n cmt_%{version}
%patch0 -p1
%patch1 -p1

%build
%{__make} -C src \
	CXX="%{__cxx}" \
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/ladspa

%{__make} -C src install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL_PLUGINS_DIR=%{_libdir}/ladspa

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README doc/*.html
%attr(755,root,root) %{_libdir}/ladspa/cmt.so
