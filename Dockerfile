FROM java:8-alpine
RUN mkdir -p /opt/kafka \
  && cd /opt/kafka \
  && apk add --update --no-cache tar curl \
  && curl --silent https://downloads.apache.org/kafka/2.8.1/kafka_2.12-2.8.1.tgz | tar -xz --strip-components=1
RUN chmod -R a=u /opt/kafka
WORKDIR /opt/kafka
VOLUME /tmp/kafka-logs /tmp/zookeeper
EXPOSE 2181 2888 3888 9092
