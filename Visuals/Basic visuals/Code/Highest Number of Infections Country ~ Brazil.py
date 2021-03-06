# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13RxPyKmONgiEjBAfzyXJ_lOSjNV-DoF1
"""

# Commented out IPython magic to ensure Python compatibility.
# Histograms for distribution analysing
import matplotlib as mpl
import seaborn as sns
from pandas import read_csv
from pandas import datetime
from matplotlib import pyplot as plt
import numpy as np
# %matplotlib inline

def parser(x):
	return datetime.strptime('202'+x, '%Y-%m-%d')

mpl.style.use('seaborn-white')
my_pallete = sns.set_palette(['#E85B80','#98C35A', '#FFAE6B', '#7FF9E3', '#D883FF', '#AB6E3B'])

brazil1 = read_csv('https://raw.githubusercontent.com/ll-cooool-j/DS-Assignment/main/Visuals/Basic%20visuals/Datasets%20of%20each%20country%20and%20Global/Highest%20Number%20of%20Infections%20Country%20~%20Brazil%20(SPSS).csv', header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
brazil1 = brazil1.drop(columns=['Infected','CFR', 'Recovery_rate', 'Mortality_rate'])

plt.rcParams.update({'figure.figsize':(21,6), 'figure.dpi':100})
brazil_dis = plt.figure()
brazil_dis.suptitle('Brazil histograms', fontsize=16)

subA = brazil_dis.add_subplot(131)
plt.hist(brazil1['Confirmed'], bins=50)
plt.gca().set(title='Confirmed Frequency Histogram', xlabel = 'Number of people', ylabel='Frequency');

subB = brazil_dis.add_subplot(132)
plt.hist(brazil1['Deaths'], bins=50)
plt.gca().set(title='Deaths Frequency Histogram', xlabel = 'Number of people', ylabel='Frequency');

subC = brazil_dis.add_subplot(133)
plt.hist(brazil1['Recovered'], bins=50)
plt.gca().set(title='Recovered Frequency Histogram', xlabel = 'Number of people', ylabel='Frequency');