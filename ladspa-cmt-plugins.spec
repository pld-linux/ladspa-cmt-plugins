%define		_name cmt
Summary:	A collection of LADSPA plugins from Computer Music Toolkit
Summary(pl):	Kolekcja wtyczek LADSPA z projektu Computer Music Toolkit
Name:		ladspa-cmt-plugins
Version:	1.15
Release:	0.1
License:	GPL
Group:		Applications/Sound
Source0:	http://www.ladspa.org/download/%{_name}_src_%{version}.tgz
# Source0-md5:	aa2f0609aca8b698625d86170c426e2c
Patch0:		%{name}-makefile.patch
URL:		http://www.ladspa.org/
BuildRequires:	ladspa-devel
BuildRequires:	libstdc++-devel
Requires:	ladspa-common
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Computer Music Toolkit (CMT) is a collection of LADSPA plugins for
use with software synthesis and recording packages on Linux.

%description -l pl
Computer Music Toolkit jest kolekcj± wtyczek LADSPA do u¿ytku z
syntezatorami programowymi i programami nagrywaj±cymi d¼wiêk pod
Linuksem.

%prep
%setup -q -n %{_name}
%patch0 -p1

%build
%{__make} -C src \
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/ladspa

%{__make} install -C src \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL_PLUGINS_DIR=%{_libdir}/ladspa

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README doc/*.html
%attr(755,root,root) %{_libdir}/ladspa/*.so
