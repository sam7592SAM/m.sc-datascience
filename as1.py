# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 10:59:00 2023

@author: User
"""

# -*- coding: utf-8 -*-


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Reading CSV files.

# 1. CSV file of Pie Chart
mlsusp = pd.read_csv("malariapie.csv", index_col=0)
print(mlsusp)

# 2. CSV file of Line Plot
mlsus = pd.read_csv("malaria.csv")
print(mlsus)

# 3. CSV file of Bar Graph
mlsusb = pd.read_csv("malariabar.csv")
print(mlsusb)

# Defining Functions

# 1. Line Plot


def line_gr(lin1, con, lbl):
    ''' Function to create lineplot. Arguements such as lin1, con, and lb1
    are passed into line_gr. 'lin1' argument is used for get the values from
    the dataframe 'mlsus', 'con' arguement is used to get the country lists
    from the dataframe and 'lb1' is an arguement to get the labels that needed
    to plot on the graph.'''
    return plt.plot(lin1["Year"], lin1[con], label=lbl)

# 2. Pie Chart


def pie_gr(p1):
    ''' Function to create pie chart. Arguement 'p1' is
    passed into pie_gr and is used to collect the values from the dataframe
    'mlsusp'.'''
    plt.figure()
    plt.pie(p1['India'], labels=p1.index, autopct='%1.f%%')
    return


# 3 Bar Graph


def bar_gr(b1, contr, cas):
    '''Function to create Bar Graph. Arguements such as b1, contr, cas
    are passed into bar_gr. 'b1' arguement is used to get the values from the
    dataframe 'mlsusb', 'contr' and 'cas' are used to get the values of the
    countries to plot in X-axis and Y-axis respectively.  '''
    plt.figure(figsize=[10, 6])
    plt.bar(b1[contr], b1[cas])
    return


# Calling Functions

# 1. Inserting values into the Line Plot from the dataframe mlsus using line_gr

line_gr(mlsus, "India", "India")
line_gr(mlsus, "Democratic Republic of the Congo", "D_Rep_Congo")
line_gr(mlsus, "Nigeria", "Nigeria")
line_gr(mlsus, "Uganda", "Uganda")
line_gr(mlsus, "Ghana", "Ghana")

# Labelling X and Y plots

plt.xlabel("Year")
plt.ylabel("No of Cases (in hundred millions)")

plt.title("Suspected Malaria Cases")  # Title to the Line Plot
plt.savefig("linegr.png")  # saving the plot in PNG format
plt.legend()
plt.show()

# 2. Retrieveing the values from the dataframe mlsusp into the Pie Chart
# using pie_gr

pie_gr(mlsusp)

plt.title("Malaria Spread in India")  # Title to the Pie Chart
plt.savefig("piegrin.png")  # saving the plot in PNG format
plt.show()


# 3. Inserting values into the Bar Graph from the dataframe mlsusb using bar_gr

bar_gr(mlsusb, "Countries", "Suspected Cases")

plt.title("Malaria Cases in 2020")  # Title to the Bar Graph

# Labelling X and Y plots

plt.xlabel("Countries")
plt.ylabel("No. of Cases (in hundred millions)")
plt.legend(loc='best')
plt.savefig("bargr.png")  # saving the plot in PNG format
plt.show()
