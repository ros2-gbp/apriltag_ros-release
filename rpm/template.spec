%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/humble/.*$
%global __requires_exclude_from ^/opt/ros/humble/.*$

Name:           ros-humble-apriltag-ros
Version:        3.2.2
Release:        3%{?dist}%{?release_suffix}
Summary:        ROS apriltag_ros package

License:        MIT
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-humble-apriltag
Requires:       ros-humble-apriltag-msgs
Requires:       ros-humble-cv-bridge
Requires:       ros-humble-image-transport
Requires:       ros-humble-rclcpp
Requires:       ros-humble-rclcpp-components
Requires:       ros-humble-sensor-msgs
Requires:       ros-humble-tf2-ros
Requires:       ros-humble-ros-workspace
BuildRequires:  eigen3-devel
BuildRequires:  ros-humble-ament-cmake
BuildRequires:  ros-humble-apriltag
BuildRequires:  ros-humble-apriltag-msgs
BuildRequires:  ros-humble-cv-bridge
BuildRequires:  ros-humble-image-transport
BuildRequires:  ros-humble-rclcpp
BuildRequires:  ros-humble-rclcpp-components
BuildRequires:  ros-humble-sensor-msgs
BuildRequires:  ros-humble-tf2-ros
BuildRequires:  ros-humble-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-humble-ament-cmake-clang-format
BuildRequires:  ros-humble-ament-cmake-cppcheck
BuildRequires:  ros-humble-ament-lint-auto
%endif

%description
AprilTag detection node

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/humble" \
    -DAMENT_PREFIX_PATH="/opt/ros/humble" \
    -DCMAKE_PREFIX_PATH="/opt/ros/humble" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/humble

%changelog
* Fri Jun 07 2024 Christian Rauch <Rauch.Christian@gmx.de> - 3.2.2-3
- Autogenerated by Bloom

* Fri Jun 07 2024 Christian Rauch <Rauch.Christian@gmx.de> - 3.2.2-2
- Autogenerated by Bloom

* Fri Jun 07 2024 Christian Rauch <Rauch.Christian@gmx.de> - 3.2.2-1
- Autogenerated by Bloom

* Fri May 31 2024 Christian Rauch <Rauch.Christian@gmx.de> - 3.2.1-1
- Autogenerated by Bloom

* Thu May 30 2024 Christian Rauch <Rauch.Christian@gmx.de> - 3.2.0-1
- Autogenerated by Bloom

* Sun Apr 02 2023 Christian Rauch <Rauch.Christian@gmx.de> - 3.1.2-1
- Autogenerated by Bloom

* Fri Jan 27 2023 Christian Rauch <Rauch.Christian@gmx.de> - 3.1.1-1
- Autogenerated by Bloom

