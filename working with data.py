# -*- coding: utf-8 -*-
"""
Created on Mon May 29 22:28:56 2023

@author: HP
"""

import pandas as pd
import csv
import matplotlib.pyplot as plt

df = pd.read_csv("ass4.csv")

grouped = df.groupby("Education Level of Mother")

aggregated = grouped["Number of Births"].sum()


description = df["Number of Births"].describe()


print(aggregated)

print(description)

plt.plot(df["Number of Births"])

plt.show()