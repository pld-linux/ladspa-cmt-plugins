%define		_name cmt
Summary:	A collection of LADSPA plugins
Summary(pl):	Kolekcja wtyczek do LADSPA
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
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Computer Music Toolkit (CMT) is a collection of LADSPA plugins for
use with software synthesis and recording packages on Linux.

%description -l pl
Computer Music Toolkit jest kolekcj± wtyczek dla LADSPA do u¿ytku z
programami syntezy programowej i nagrywaj±cymi pod Linuxem.

%prep
%setup -q -n %{_name}
%patch0 -p1

%build
cd src
%{__make} OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_libdir}/ladspa

cd src
%{__make} DESTDIR="$RPM_BUILD_ROOT" install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README doc/*.html
%attr(755,root,root) %{_libdir}/ladspa/*.so
