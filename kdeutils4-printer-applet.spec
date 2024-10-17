%define oname printer-applet

Name:		kdeutils4-printer-applet
Summary:	View current print jobs and configure new printers
Version:	4.9.4
Release:	1
Group:		Graphical desktop/KDE
License:	LGPLv2
URL:		https://utils.kde.org/projects/%{oname}
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{oname}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	python-kde4
BuildRequires:	system-config-printer
BuildRequires:	python-cups
BuildRequires:	python-devel
Requires:	python-kde4
Requires:	python-cups
Requires:	python-qt4
Requires:	python-dbus
Requires:	system-config-printer
Provides:	printer-applet
BuildArch:	noarch

%description
Printer Applet is a system tray utility that shows current print jobs,
shows printer warnings and errors and shows when printers that have
been plugged in for the first time are being auto-configured by
hal-cups-utils.

%files
%doc %{_kde_docdir}/HTML/en/printer-applet
%{_kde_bindir}/printer-applet
%{_kde_appsdir}/printer-applet
%{_kde_autostart}/printer-applet.desktop

#----------------------------------------------------------------------

%prep
%setup -q -n %{oname}-%{version}

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.2-2
- New version 4.9.2
- Should be noarch package

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.1-1
- New version 4.9.1

* Tue Aug 14 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.0-1
- New version 4.9.0

* Sun Jul 22 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.8.97-1
- New version 4.8.97

* Sun Jul 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.8.95-1
- New version 4.8.95

* Fri Jun 08 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 4.8.4-1
- update to 4.8.4

* Thu May 10 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 4.8.3-1
- update to 4.8.3

* Sun Mar 11 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 4.8.2-1
- update to 4.8.2

* Sun Mar 11 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 4.8.1-1
- update to 4.8.1

* Thu Jan 19 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.8.0-1
+ Revision: 762419
- New upstream tarball

* Fri Jan 06 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.97-1
+ Revision: 758120
- New upstream tarball

* Thu Nov 24 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.80-1
+ Revision: 733049
- Import printer-applet
- Create folder

