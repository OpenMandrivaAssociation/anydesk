Summary: The world's fastest remote desktop application
Name:    anydesk
Version: 6.2.1
Release: %mkrel 1
License: Proprietary
Group:   Applications/Internet
Url:     https://anydesk.com
Source0: https://download.anydesk.com/linux/anydesk-%{version}-amd64.tar.gz

ExclusiveArch: %{x86_64}

Requires: adwaita-gtk2-theme
Requires: lib64gtk-modules2.0
Requires: lib64gtkglext-x11_1.0_0

%description
AnyDesk is the fastest remote desktop software on the market. It allows
for new usage scenarios and applications that have not been possible with
current remote desktop software.

%prep
%autosetup -n %{name}-%{version}

%install
mkdir -p %{buildroot}%{_bindir} \
         %{buildroot}%{_datadir}/applications \
         %{buildroot}%{_iconsdir}

cp -a %{name} %{buildroot}%{_bindir}/
cp -a %{name}.desktop %{buildroot}%{_datadir}/applications/
cp -ar icons/* %{buildroot}%{_iconsdir}/

%files
# init/systemd and polkit stuff left out on purpose.
# The service, as configured by the vendor, runs as root!
%license copyright
%{_bindir}/%{name}
%{_datadir}/applications/
%{_iconsdir}/hicolor/*/apps/%{name}.*
