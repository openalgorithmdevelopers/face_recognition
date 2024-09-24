#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 09:09:15 2024

@author: upes
"""

import time

prev = time.time()

myDict = {'n':0}

t = int(time.time() - prev)
myDict.update({'bhupi': t})
t = int(time.time() - prev)
myDict.update({'raj': t})

time.sleep(3)

t = int(time.time() - prev)
myDict.update({'Tanay': t})

time.sleep(3)

t = int(time.time() - prev)

nameList = myDict.keys()
for d in nameList:
    if d == 'Tanay':
        print(myDict[d])

print(myDict)
