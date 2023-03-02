# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 10:59:00 2023

@author: User
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 13:59:02 2023

@author: User
"""
#importing 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Reading CSV files for plotting Line, Pie and Bar Graph
mlsusp = pd.read_csv ("malariapie.csv", index_col=0)
print (mlsusp)

mlsus = pd.read_csv ("malaria.csv")
print (mlsus)

mlsusb = pd.read_csv("malariabar.csv")
print(mlsusb)

# Defining Functions

# 1. Line Graph
def line_gr(lin1, con, lbl):
    return plt.plot (lin1 ["Year"], lin1 [con], label = lbl)
    
# 2. Pie Graph
def pie_gr (p1, lb2):
    plt.figure()
    plt.pie(p1['India'], labels = p1.index, autopct='%1.f%%')
    return

# 3 Bar Graph
def bar_gr(b1,contr,cas):
    plt.figure(figsize=[10, 6])
    plt.bar(b1[contr], b1[cas])
    return


# Caliing functions
# 1. Calling Line Graph using line_gr

line_gr(mlsus, "India", "India")
line_gr(mlsus, "Democratic Republic of the Congo", "D_Rep_Congo")
line_gr(mlsus, "Nigeria", "Nigeria")
line_gr(mlsus, "Uganda", "Uganda")
line_gr(mlsus, "Ghana", "Ghana")

plt.xlabel("Year")
plt.ylabel("No of Cases")
plt.title("Suspected Malaria Cases")
plt.savefig("linegr.png")
plt.legend()

# 2. Calling Pie Graph using pie_gr

pie_gr (mlsusp, ["2010", "2011", "2012", "2013","2014","2015","2016","2017","2018","2019","2020"])

plt.title("Malaria Spread in India")
plt.savefig("piegr.png")
plt.show()

#3. Calling Bar Graph using bar_gr

bar_gr (mlsusb, "Countries", "Suspected Cases")

plt.title("Malaria Cases in 2020")
plt.xlabel("Countries")
plt.ylabel("No. of Cases")
plt.legend(loc='best')
plt.savefig("bargr.png")
plt.show()









