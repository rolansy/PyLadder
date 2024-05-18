# -*- coding: utf-8 -*-
"""
Created on Sat May 18 11:20:46 2024

@author: ronal
"""

import pandas as pd

# Create a list of dictionaries
data = [
    {"student_id": 101, "name": "Ulysses", "age": 13},
    {"student_id": 53, "name": "William", "age": 10},
    {"student_id": 128, "name": "Henry", "age": 6},
    {"student_id": 3, "name": "Henry", "age": 11},
]

# Create a DataFrame
df = pd.DataFrame(data)

# Print the DataFrame
print(df)

x=df[df["student_id"]==128][['student_id','name','age']]

print(x)
