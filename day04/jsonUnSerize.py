#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__mtime__ = '2018/6/4'
"""
import json
f = open("jsonSave.txt","r")
data = json.loads(f.read())
print(data["age"])
print(data["nation"])