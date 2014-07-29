%global cartridgedir %{_libexecdir}/openshift/cartridges/egovframe

Summary:       Provides egovframe3.0
Name:          openpaas-cartridge-egovframe
Version: 0.0.1.1
Release:       1%{?dist}
Group:         Development/FrameWork
License:       ASL 2.0
URL:           http://openpaas.cloudsc.kr
Source0:       https://github.com/kikimans/openpaas-cartridge-egovframe
Requires:      facter
Requires:      rubygem(openshift-origin-node)
Requires:      openshift-origin-node-util
Requires:      lsof
Requires:      java-1.7.0-openjdk
Requires:      java-1.7.0-openjdk-devel
%if 0%{?rhel}
Requires:      maven3
%endif
%if 0%{?fedora}
Requires:      maven
%endif
BuildRequires: jpackage-utils
BuildArch:     noarch

%description
Provides EgovFrameWork 3.0 & Tomcat7.0 support to Jyes. (Cartridge Format V2)

%prep
%setup -q

%build
%__rm %{name}.spec

%install
%__mkdir -p %{buildroot}%{cartridgedir}
%__cp -r * %{buildroot}%{cartridgedir}

%post
# To modify an alternative you should:
# - remove the previous version if it's no longer valid
# - install the new version with an increased priority
# - set the new version as the default to be safe

%if 0%{?rhel}
alternatives --install /etc/alternatives/maven-3.0 maven-3.0 /usr/share/java/apache-maven-3.0.3 100
alternatives --set maven-3.0 /usr/share/java/apache-maven-3.0.3
%endif

%if 0%{?fedora}
alternatives --remove maven-3.0 /usr/share/java/apache-maven-3.0.3
alternatives --install /etc/alternatives/maven-3.0 maven-3.0 /usr/share/maven 102
alternatives --set maven-3.0 /usr/share/maven
%endif

alternatives --remove tomcat-2.0 /usr/share/tomcat7
alternatives --install /etc/alternatives/tomcat-2.0 tomcat-2.0 /usr/share/tomcat7 102
alternatives --set tomcat-2.0 /usr/share/tomcat7

%files
%dir %{cartridgedir}
%attr(0755,-,-) %{cartridgedir}/bin/
%{cartridgedir}
%doc %{cartridgedir}/README.md
%doc %{cartridgedir}/COPYRIGHT
%doc %{cartridgedir}/LICENSE


