FROM java:8u111-jdk-alpine
RUN mkdir -p /opt/kafka \
  && apk add --update --no-cache bash curl tar
WORKDIR /opt/kafka
RUN chmod -R a=u /opt/kafka
RUN curl --silent https://downloads.apache.org/kafka/3.2.3/kafka_2.12-3.2.3.tgz | tar -xz --strip-components=1
VOLUME /tmp/kafka-logs /tmp/zookeeper
EXPOSE 2181 2888 3888 9092
