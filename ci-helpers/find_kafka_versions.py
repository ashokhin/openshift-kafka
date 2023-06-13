#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import re
import sys
import urllib.request
from html.parser import HTMLParser


logging.getLogger(__name__).addHandler(logging.NullHandler())


class Parser(HTMLParser):
    def handle_data(self, data):
        global all_data
        if re.match(parser_regex, data):
            all_data.append(data)


def get_http_data(url: str):
    try:
        return urllib.request.urlopen(url).read().decode()
    except:
        logging.exception("Failed open URL '{}'".format(url))
        sys.exit(1)


def main():
    logging.basicConfig(format=u'[%(asctime)s][%(levelname)-8s][PID:%(process)d] %(funcName)s.%(lineno)d: %(message)s', 
                        level=logging.ERROR, stream=sys.stdout)
    global parser_regex, all_data
    kafka_base_url = "https://downloads.apache.org/kafka/"
    kafka_base_version_regex = r'^[0-9]+\.[0-9]+\.[0-9]+\/$'
    kafka_archive_regex = r'^kafka_[0-9]+\.[0-9]+-[0-9]+\.[0-9]+\.[0-9]+\.tgz$'
    kafka_version_regex = r'[0-9]+\.[0-9]+-[0-9]+\.[0-9]+\.[0-9]+'

    all_data = []
    parser_regex = kafka_base_version_regex
    parser = Parser()
    parser.feed(get_http_data(kafka_base_url))
    kafka_base_versions = all_data
    all_data = []
    kafka_versions_arr = []

    for kafka_version in kafka_base_versions:
        version_url = "{}{}".format(kafka_base_url, kafka_version)
        parser_regex = kafka_archive_regex
        parser.feed(get_http_data(version_url))
        kafka_archives = all_data
        all_data = []
        for kafka_archive in kafka_archives:
            kafka_full_version = re.search(kafka_version_regex, kafka_archive).group(0)
            kafka_versions_arr.append({
                'version': kafka_full_version,
                'download_url': "{}{}{}".format(kafka_base_url, kafka_version, kafka_archive),
            })
    
    print(kafka_versions_arr)


if __name__ == '__main__':
    sys.exit(main())