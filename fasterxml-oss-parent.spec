%{?scl:%scl_package fasterxml-oss-parent}
%{!?scl:%global pkg_name %{name}}

%global oname oss-parent
Name:          %{?scl_prefix}fasterxml-oss-parent
Version:       26
Release:       3.3%{?dist}
Summary:       FasterXML parent pom
License:       ASL 2.0
URL:           http://fasterxml.com/
Source0:       https://github.com/FasterXML/oss-parent/archive/oss-parent-%{version}.tar.gz

BuildRequires: %{?scl_prefix}maven-local
BuildRequires: %{?scl_prefix}mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: %{?scl_prefix}mvn(org.codehaus.mojo:build-helper-maven-plugin)

BuildArch:     noarch

%description
FasterXML is the business behind the Woodstox streaming XML parser,
Jackson streaming JSON parser, the Aalto non-blocking XML parser, and
a growing family of utility libraries and extensions.

FasterXML offers consulting services for adoption, performance tuning,
and extension.

This package contains the parent pom file for FasterXML.com projects.

%prep
%setup -q -n %{oname}-%{oname}-%{version}

%pom_remove_plugin org.sonatype.plugins:nexus-maven-plugin
%pom_remove_plugin :maven-scm-plugin
%pom_remove_plugin org.codehaus.mojo:jdepend-maven-plugin
%pom_remove_plugin org.codehaus.mojo:taglist-maven-plugin
# org.kathrynhuxtable.maven.wagon:wagon-gitsite:0.3.1
%pom_xpath_remove "pom:build/pom:extensions"
# remove unavailable com.google.doclava doclava 1.0.3
%pom_xpath_remove "pom:reporting/pom:plugins/pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:configuration"
%pom_xpath_inject "pom:reporting/pom:plugins/pom:plugin[pom:artifactId='maven-javadoc-plugin']" '
<configuration>
  <encoding>UTF-8</encoding>
  <quiet>true</quiet>
  <source>${javac.src.version}</source>
</configuration>'

%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-site-plugin

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%doc README.creole
%license LICENSE NOTICE

%changelog
* Mon Aug 07 2017 Michael Simacek <msimacek@redhat.com> - 26-3.3
- Fix incorrect license tag

* Thu Jun 22 2017 Michael Simacek <msimacek@redhat.com> - 26-3.2
- Mass rebuild 2017-06-22

* Wed Jun 21 2017 Java Maintainers <java-maint@redhat.com> - 26-3.1
- Automated package import and SCL-ization

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 02 2017 Michael Simacek <msimacek@redhat.com> - 26-2
- Remove site-plugin from build

* Mon Aug 22 2016 gil cattaneo <puntogil@libero.it> 26-1
- update to 26

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Oct 25 2015 gil cattaneo <puntogil@libero.it> 24-2
- disable maven-enforcer-plugin support

* Mon Sep 28 2015 gil cattaneo <puntogil@libero.it> 24-1
- update to 24

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 18e-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jan 31 2015 gil cattaneo <puntogil@libero.it> 18e-1
- update to 18e

* Wed Jul 02 2014 gil cattaneo <puntogil@libero.it> 16-2
- remove com.google.code.maven-replacer-plugin:replacer references 

* Wed Jul 02 2014 gil cattaneo <puntogil@libero.it> 16-1
- update to 16

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 11-3
- Rebuild to regenerate Maven auto-requires

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 16 2013 gil cattaneo <puntogil@libero.it> 11-1
- update to 11

* Sat Jul 06 2013 gil cattaneo <puntogil@libero.it> 10-2
- switch to XMvn
- minor changes to adapt to current guideline

* Tue May 07 2013 gil cattaneo <puntogil@libero.it> 10-1
- update to 10

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 4-2
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Oct 24 2012 gil cattaneo <puntogil@libero.it> 4-1
- update to 4

* Thu Sep 13 2012 gil cattaneo <puntogil@libero.it> 3-1
- initial rpm
