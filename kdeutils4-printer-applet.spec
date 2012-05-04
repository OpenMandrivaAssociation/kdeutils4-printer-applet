%define oname printer-applet

Name:    kdeutils4-printer-applet
Summary: View current print jobs and configure new printers
Version: 4.8.3
Release: 1
Group: Graphical desktop/KDE
License: LGPLv2
URL:     http://utils.kde.org/projects/%oname
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%{oname}-%version.tar.xz

BuildRequires: kdelibs4-devel >= 2:%{version}
BuildRequires: python-kde4
BuildRequires: system-config-printer
BuildRequires: python-cups
BuildRequires: python-devel

Requires: python-kde4 >= 1:4.1.0
Requires: python-cups
Requires: python-qt4
Requires: python-dbus
Requires: system-config-printer

%description
Printer Applet is a system tray utility that shows current print jobs,
shows printer warnings and errors and shows when printers that have
been plugged in for the first time are being auto-configured by
hal-cups-utils.

%files
%_kde_bindir/printer-applet
%_kde_appsdir/printer-applet
%_kde_datadir/autostart/printer-applet.desktop
%doc %_kde_docdir/HTML/en/printer-applet

#----------------------------------------------------------------------

%prep
%setup -q -n %{oname}-%version

%build
%cmake_kde4
	
%make

%install
%makeinstall_std -C build

