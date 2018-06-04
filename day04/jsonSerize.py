#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__mtime__ = '2018/6/4'
"""
import json
info = {
    "name":"liujiefei",
    "age":23,
    "nation":"china"
}
f = open("jsonSave.txt","w")
f.write(json.dumps(info))
print(json.dumps(info))