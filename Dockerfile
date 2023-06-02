FROM java:openjdk-8u111-jdk-alpine
RUN mkdir -p /opt/kafka \
  && apk add --update --no-cache bash curl tar
WORKDIR /opt/kafka
RUN chmod -R a=u /opt/kafka
RUN curl -L --silent https://downloads.apache.org/kafka/3.1.2/kafka_2.12-3.1.2.tgz | tar -xz --strip-components=1
VOLUME /tmp/kafka-logs /tmp/zookeeper
EXPOSE 2181 2888 3888 9092
