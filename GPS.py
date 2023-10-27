# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 03:52:25 2023

@author: ronal
"""

import csv
with open ('route.csv','r') as f:
    rr=csv.reader(f)
    
    for r in rr:
        lat=float(r[0])
        long=float(r[1])
        print(lat)
        print(long)
        print(lat+long)
        