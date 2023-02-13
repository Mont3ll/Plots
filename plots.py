
import pandas as pd
data=pd.read_csv("gapminder_with_codes.csv")
data_2007=data[data['year']==2007]

import matplotlib.pyplot as plt

fig, ax=plt.subplots()
ax.scatter(x=data_2007['gdpPercap'], y=data_2007['lifeExp'], alpha=0.8)
ax.set_xlabel('GDP (USD) per capita')
ax.set_ylabel('life expectancy (years)')

fig, ax=plt.subplots()

ax.scatter(x=data_2007['gdpPercap'], y=data_2007['lifeExp'], alpha=0.9)
ax.set_xscale("log")
ax.set_xlabel('GDP (USD) Per Capita')
ax.set_ylabel('Life expectancy (years)')

#plots for publication
#make tickmarks and axis label larger

fig, ax=plt.subplots()
ax.scatter(x=data_2007['gdpPercap'], y=data_2007['lifeExp'], alpha=0.8)
ax.set_ylabel('Life expectancy (years)', fontsize=15)
ax.set_xlabel('GDP(USD) per Capita', fontsize=15)
ax.set_title('Some title', fontsize=15)

ax.tick_params(which='major', length=10)
ax.tick_params(which ='minor', length=10)
ax.tick_params(labelsize=15)

#violin plot

import numpy as np
import seaborn as sns

plt.figure(figsize=(12,96), dpi=200)
sns.violinplot(data=data_2007, x= data['lifeExp'], y=data['country'], scale='count')

plt.figure(figsize=(12,96), dpi=200)
sns.violinplot(data=data_2007, x=data['gdpPercap'], y=data['country'], scale='count')

plt.figure(figsize=(12,96), dpi=200)
sns.violinplot(data=data_2007, x=data['pop'], y=data['country'], scale='count')
