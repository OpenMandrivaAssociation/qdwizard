Name:          qdwizard
Summary:       Simple Java Swing Wizard API
Version:       1.9
Release:       %mkrel 4
License:       LGPL
Group:	       Sound
Source0:       %name-%version.tar.bz2
Patch0:        qdwizard-1.9-fix-build.patch
URL: 	       http://qdwizard.sourceforge.net/
BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: ant
BuildRequires: java-devel-gcj

%description
* Designed to minimize required code. Only few methods to implement.
* Simple design, only two classes visible by the programmer.
* I18n support for action buttons (en, fr, de, sp, ca, nl for the moment).
* Full branching support, can implement any wizard cinematic.
* Error management using the simple setProblem() method.
* Supports Wizard images natively and resizes image automaticaly.
* Ultra light API: only few KB.
* Actively supported by the Jajuk team.
* Learning curve of 15 minutes maximum.
* Real world samples provided (jajuk classes).

%files 
%defattr(-,root,root)
%{_javadir}/%name-%version.jar
%{_javadir}/%name.jar

#--------------------------------------------------------------------

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java

%description javadoc
Javadoc for %{name}.

%files javadoc
%defattr(-,root,root,-)
%{_javadocdir}/*

#--------------------------------------------------------------------

%prep
rm -fr %buildroot
%setup -q -n QDWizard
%patch0 -p0

%build

%{ant} 

%install

# jars
install -dm 755 %buildroot%{_javadir}
install -m644 qdwizard_releases/qdwizard-1.9/qdwizard-1.9.jar -D %{buildroot}%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# javadoc
install -d %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -r dist/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%clean
rm -fr %buildroot
