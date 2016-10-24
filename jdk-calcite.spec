Name     : jdk-calcite
Version  : 1.2.0
Release  : 1
URL      : http://repo2.maven.org/maven2/org/apache/calcite/calcite/1.2.0-incubating/calcite-1.2.0-incubating.pom
Source0  : http://repo2.maven.org/maven2/org/apache/calcite/calcite/1.2.0-incubating/calcite-1.2.0-incubating.pom
Source1  : http://repo2.maven.org/maven2/org/apache/calcite/calcite-avatica/1.2.0-incubating/calcite-avatica-1.2.0-incubating.jar
Source2  : http://repo2.maven.org/maven2/org/apache/calcite/calcite-avatica/1.2.0-incubating/calcite-avatica-1.2.0-incubating.pom
Source3  : http://repo2.maven.org/maven2/org/apache/calcite/calcite-avatica-server/1.2.0-incubating/calcite-avatica-server-1.2.0-incubating.jar
Source4  : http://repo2.maven.org/maven2/org/apache/calcite/calcite-avatica-server/1.2.0-incubating/calcite-avatica-server-1.2.0-incubating.pom
Source5  : http://repo2.maven.org/maven2/org/apache/calcite/calcite-core/1.2.0-incubating/calcite-core-1.2.0-incubating.jar
Source6  : http://repo2.maven.org/maven2/org/apache/calcite/calcite-core/1.2.0-incubating/calcite-core-1.2.0-incubating.pom
Source7  : http://repo2.maven.org/maven2/org/apache/calcite/calcite-example-csv/1.2.0-incubating/calcite-example-csv-1.2.0-incubating.jar
Source8  : http://repo2.maven.org/maven2/org/apache/calcite/calcite-example-csv/1.2.0-incubating/calcite-example-csv-1.2.0-incubating.pom
Source9  : http://repo2.maven.org/maven2/org/apache/calcite/calcite-example/1.2.0-incubating/calcite-example-1.2.0-incubating.pom
Source10 : http://repo2.maven.org/maven2/org/apache/calcite/calcite-mongodb/1.2.0-incubating/calcite-mongodb-1.2.0-incubating.jar
Source11 : http://repo2.maven.org/maven2/org/apache/calcite/calcite-mongodb/1.2.0-incubating/calcite-mongodb-1.2.0-incubating.pom
Source12 : http://repo2.maven.org/maven2/org/apache/calcite/calcite-plus/1.2.0-incubating/calcite-plus-1.2.0-incubating.jar
Source13 : http://repo2.maven.org/maven2/org/apache/calcite/calcite-plus/1.2.0-incubating/calcite-plus-1.2.0-incubating.pom
Source14 : http://repo2.maven.org/maven2/org/apache/calcite/calcite-spark/1.2.0-incubating/calcite-spark-1.2.0-incubating.jar
Source15 : http://repo2.maven.org/maven2/org/apache/calcite/calcite-spark/1.2.0-incubating/calcite-spark-1.2.0-incubating.pom
Source16 : http://repo2.maven.org/maven2/org/apache/calcite/calcite-splunk/1.2.0-incubating/calcite-splunk-1.2.0-incubating.jar
Source17 : http://repo2.maven.org/maven2/org/apache/calcite/calcite-splunk/1.2.0-incubating/calcite-splunk-1.2.0-incubating.pom
Source18 : http://repo2.maven.org/maven2/org/apache/calcite/calcite-ubenchmark/1.2.0-incubating/calcite-ubenchmark-1.2.0-incubating.jar
Source19 : http://repo2.maven.org/maven2/org/apache/calcite/calcite-ubenchmark/1.2.0-incubating/calcite-ubenchmark-1.2.0-incubating.pom

Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

# Rename files
mv %{SOURCE0} %{buildroot}/usr/share/maven-poms/calcite.pom

mv %{SOURCE1} %{buildroot}/usr/share/java/calcite-avatica.jar
mv %{SOURCE2} %{buildroot}/usr/share/maven-poms/calcite-avatica.pom

mv %{SOURCE3} %{buildroot}/usr/share/java/calcite-avatica-server.jar
mv %{SOURCE4} %{buildroot}/usr/share/maven-poms/calcite-avatica-server.pom

mv %{SOURCE5} %{buildroot}/usr/share/java/calcite-core.jar
mv %{SOURCE6} %{buildroot}/usr/share/maven-poms/calcite-core.pom

mv %{SOURCE7} %{buildroot}/usr/share/java/calcite-example-csv.jar
mv %{SOURCE8} %{buildroot}/usr/share/maven-poms/calcite-example-csv.pom

mv %{SOURCE9} %{buildroot}/usr/share/maven-poms/calcite-example.pom

mv %{SOURCE10} %{buildroot}/usr/share/java/calcite-mongodb.jar
mv %{SOURCE11} %{buildroot}/usr/share/maven-poms/calcite-mongodb.pom

mv %{SOURCE12} %{buildroot}/usr/share/java/calcite-plus.jar
mv %{SOURCE13} %{buildroot}/usr/share/maven-poms/calcite-plus.pom

mv %{SOURCE14} %{buildroot}/usr/share/java/calcite-spark.jar
mv %{SOURCE15} %{buildroot}/usr/share/maven-poms/calcite-spark.pom

mv %{SOURCE16} %{buildroot}/usr/share/java/calcite-splunk.jar
mv %{SOURCE17} %{buildroot}/usr/share/maven-poms/calcite-splunk.pom

mv %{SOURCE18} %{buildroot}/usr/share/java/calcite-ubenchmark.jar
mv %{SOURCE19} %{buildroot}/usr/share/maven-poms/calcite-ubenchmark.pom

# Creates metadata
for e in calcite calcite-avatica calcite-avatica-server calcite-core \
calcite-example-csv calcite-example calcite-mongodb \
calcite-plus calcite-spark calcite-splunk calcite-ubenchmark
do
	
	python3 /usr/share/java-utils/maven_depmap.py \
	-n "" \
	--pom-base %{buildroot}/usr/share/maven-poms \
	--jar-base %{buildroot}/usr/share/java \
	%{buildroot}/usr/share/maven-metadata/$e.xml \
	%{buildroot}/usr/share/maven-poms/$e.pom \
	%{buildroot}/usr/share/java/$e.jar
done

%files
%defattr(-,root,root,-)
/usr/share/java/calcite-avatica-server.jar
/usr/share/java/calcite-avatica.jar
/usr/share/java/calcite-core.jar
/usr/share/java/calcite-example-csv.jar
/usr/share/java/calcite-mongodb.jar
/usr/share/java/calcite-plus.jar
/usr/share/java/calcite-spark.jar
/usr/share/java/calcite-splunk.jar
/usr/share/java/calcite-ubenchmark.jar
/usr/share/maven-metadata/calcite-avatica-server.xml
/usr/share/maven-metadata/calcite-avatica.xml
/usr/share/maven-metadata/calcite-core.xml
/usr/share/maven-metadata/calcite-example-csv.xml
/usr/share/maven-metadata/calcite-example.xml
/usr/share/maven-metadata/calcite-mongodb.xml
/usr/share/maven-metadata/calcite-plus.xml
/usr/share/maven-metadata/calcite-spark.xml
/usr/share/maven-metadata/calcite-splunk.xml
/usr/share/maven-metadata/calcite-ubenchmark.xml
/usr/share/maven-metadata/calcite.xml
/usr/share/maven-poms/calcite-avatica-server.pom
/usr/share/maven-poms/calcite-avatica.pom
/usr/share/maven-poms/calcite-core.pom
/usr/share/maven-poms/calcite-example-csv.pom
/usr/share/maven-poms/calcite-example.pom
/usr/share/maven-poms/calcite-mongodb.pom
/usr/share/maven-poms/calcite-plus.pom
/usr/share/maven-poms/calcite-spark.pom
/usr/share/maven-poms/calcite-splunk.pom
/usr/share/maven-poms/calcite-ubenchmark.pom
/usr/share/maven-poms/calcite.pom
