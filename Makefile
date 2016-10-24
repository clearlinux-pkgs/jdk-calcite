PKG_NAME := jdk-calcite
URL := http://repo2.maven.org/maven2/org/apache/calcite/calcite/1.2.0-incubating/calcite-1.2.0-incubating.pom
ARCHIVES := http://repo2.maven.org/maven2/org/apache/calcite/calcite-avatica/1.2.0-incubating/calcite-avatica-1.2.0-incubating.jar %{buildroot} \
http://repo2.maven.org/maven2/org/apache/calcite/calcite-avatica/1.2.0-incubating/calcite-avatica-1.2.0-incubating.pom %{buildroot} \
http://repo2.maven.org/maven2/org/apache/calcite/calcite-avatica-server/1.2.0-incubating/calcite-avatica-server-1.2.0-incubating.jar %{buildroot} \
http://repo2.maven.org/maven2/org/apache/calcite/calcite-avatica-server/1.2.0-incubating/calcite-avatica-server-1.2.0-incubating.pom %{buildroot} \
http://repo2.maven.org/maven2/org/apache/calcite/calcite-core/1.2.0-incubating/calcite-core-1.2.0-incubating.jar %{buildroot} \
http://repo2.maven.org/maven2/org/apache/calcite/calcite-core/1.2.0-incubating/calcite-core-1.2.0-incubating.pom %{buildroot} \
http://repo2.maven.org/maven2/org/apache/calcite/calcite-example-csv/1.2.0-incubating/calcite-example-csv-1.2.0-incubating.jar %{buildroot} \
http://repo2.maven.org/maven2/org/apache/calcite/calcite-example-csv/1.2.0-incubating/calcite-example-csv-1.2.0-incubating.pom %{buildroot} \
http://repo2.maven.org/maven2/org/apache/calcite/calcite-example/1.2.0-incubating/calcite-example-1.2.0-incubating.pom %{buildroot} \
http://repo2.maven.org/maven2/org/apache/calcite/calcite-mongodb/1.2.0-incubating/calcite-mongodb-1.2.0-incubating.jar %{buildroot} \
http://repo2.maven.org/maven2/org/apache/calcite/calcite-mongodb/1.2.0-incubating/calcite-mongodb-1.2.0-incubating.pom %{buildroot} \
http://repo2.maven.org/maven2/org/apache/calcite/calcite-plus/1.2.0-incubating/calcite-plus-1.2.0-incubating.jar %{buildroot} \
http://repo2.maven.org/maven2/org/apache/calcite/calcite-plus/1.2.0-incubating/calcite-plus-1.2.0-incubating.pom %{buildroot} \
http://repo2.maven.org/maven2/org/apache/calcite/calcite-spark/1.2.0-incubating/calcite-spark-1.2.0-incubating.jar %{buildroot} \
http://repo2.maven.org/maven2/org/apache/calcite/calcite-spark/1.2.0-incubating/calcite-spark-1.2.0-incubating.pom %{buildroot} \
http://repo2.maven.org/maven2/org/apache/calcite/calcite-splunk/1.2.0-incubating/calcite-splunk-1.2.0-incubating.jar %{buildroot} \
http://repo2.maven.org/maven2/org/apache/calcite/calcite-splunk/1.2.0-incubating/calcite-splunk-1.2.0-incubating.pom %{buildroot} \
http://repo2.maven.org/maven2/org/apache/calcite/calcite-ubenchmark/1.2.0-incubating/calcite-ubenchmark-1.2.0-incubating.jar %{buildroot} \
http://repo2.maven.org/maven2/org/apache/calcite/calcite-ubenchmark/1.2.0-incubating/calcite-ubenchmark-1.2.0-incubating.pom %{buildroot} \

include ../common/Makefile.common
