#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = "Shobhit Sharma"
__copyright__ = "TweetTracker. Copyright (c) Arizona Board of Regents on behalf of Arizona State University"
"""
import datetime


class TCDateInfo(object):
    def __init__(self):
        self.d = datetime.datetime.now()
        self.wordcount = {}

    def __cmp__(self, other):
        if other.d > self.d:
            return -1
        elif other.d < self.d:
            return 1
        else:
            return 0