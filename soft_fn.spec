Name:           soft_fn
Version:        1.0
Release:        1%{?dist}
Summary:        Chromebook-like search key behaviour on both Wayland and Xorg.

License:        GPLv3
URL:            https://github.com/metaquanta/soft_fn
Source0:        https://github.com/metaquanta/soft_fn/archive/refs/tags/v%{version}.tar.gz

%description
soft-fn reproduces the behavior of the Chromebook keyboard's Search key in linux.
It uses an evdev uinput device, such that it works in Xorg, Wayland, and virtual consoles.
In addition to Chromebook fn keys, caps lock is activated via Alt+Search (meta/super).

%prep
%setup -q

%build
make

%install
install -D -m 0755 soft_fn %{buildroot}%{_sbindir}/soft_fn
install -D soft-fn.service %{buildroot}%{_unitdir}/soft-fn.service
install -D -m 0755 launch.sh %{buildroot}%{_datadir}/soft_fn/launch.sh
install 99-disable-power-button.rules %{buildroot}%{_datadir}/soft_fn

%post
%systemd_post soft-fn.service

%postun
%systemd_postun_with_restart soft-fn.service

%files
%license LICENSE
%{_sbindir}/soft_fn
%{_unitdir}/soft-fn.service
/usr/share/soft_fn/launch.sh
/usr/share/soft_fn/99-disable-power-button.rules
