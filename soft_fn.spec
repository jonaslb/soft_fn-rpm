Name: soft_fn
Version: git20210209
Release: 1%{?dist}
Summary: Chromebook-like search key behaviour on both Wayland and Xorg.

License: GPLv3
URL: https://github.com/metaquanta/soft_fn
%define commit 6e42f468edab1414e68f4ff9c41f5947567dfca6
Source0: https://github.com/metaquanta/soft_fn/archive/%{commit}.tar.gz
Patch0: systemd-udevd.patch

BuildRequires: gcc make systemd systemd-rpm-macros
Requires: systemd
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
soft-fn reproduces the behavior of the Chromebook keyboard's Search key in linux.
It uses an evdev uinput device, such that it works in Xorg, Wayland, and virtual consoles.
In addition to Chromebook fn keys, caps lock is activated via Alt+Search (meta/super).

%global debug_package %{nil}

%prep
%setup -q -n soft_fn-%{commit}
%patch0 -p1

%build
make

%install
install -D -m 0755 soft_fn %{buildroot}%{_sbindir}/soft_fn
install -D -m 0644 soft-fn.service %{buildroot}%{_unitdir}/soft-fn.service
install -D -m 0755 launch.sh %{buildroot}%{_datadir}/soft_fn/launch.sh
install -m 0644 99-disable-power-button.rules %{buildroot}%{_datadir}/soft_fn

%post
%systemd_post soft-fn.service

%preun
%systemd_preun soft-fn.service

%postun
%systemd_postun_with_restart soft-fn.service

%files
%license LICENSE
%{_sbindir}/soft_fn
%{_unitdir}/soft-fn.service
/usr/share/soft_fn/launch.sh
/usr/share/soft_fn/99-disable-power-button.rules
