#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess

tags_list = subprocess.run('git tag -l', shell=True, capture_output=True).stdout.decode().splitlines()

print(tags_list)
