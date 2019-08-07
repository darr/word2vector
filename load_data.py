#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : load_data.py
# Create date : 2019-08-07 15:45
# Modified date : 2019-08-07 16:06
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

class DataLoader:
    def __init__(self):
        self.datafile = 'data/data.txt'
        self.dataset = self.load_data()

    def load_data(self):
        dataset = []
        for line in open(self.datafile):
            line = line.strip().split(',')
            dataset.append([word for word in line[1].split(' ') if 'nbsp' not in word and len(word) < 11])
        return dataset
