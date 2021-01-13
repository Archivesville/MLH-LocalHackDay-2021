import pandas as pd 
import numpy as numpy
import matplotlib.pyplot as plt

Mydf = pd.read_csv("C:\state_wise.csv", skiprows=1, names=['State', 'Confirmed', 'Recovered', 'Deaths', 'Active', 'State_code', 'Population', 'Area(per sq km)'])
print('The state wise COVID-19 data for October 29, 2020 is -\n\n', Mydf)

highe = Mydf[Mydf['Confirmed'].max()==Mydf['Confirmed']]
actv = Mydf[Mydf['Active'].max()==Mydf['Active']]
confirm = Mydf['Confirmed'].sum()
recovered = Mydf['Recovered'].sum()
death = Mydf['Deaths'].sum()
active = Mydf['Active'].sum()

print('\n\n Overall data of India on October 29 is - \nConfirmed: ', confirm, '\nDeaths: ', death, '\nRecovered ', recovered, '\nActive: ', active)
print('\n The state with highest confirmed case is = \n', highe)
print('\n The state with the highest recovered cases is = \n', actv)

#Statewise number of confirmed cases in India
Mydf= Mydf.sort_values(by=['Confirmed'], ascending=False)
plt.figure(figsize=(12, 8), dpi=80)
plt.bar(Mydf['State'][:5], Mydf['Confirmed'][:5],       
        align='center', color='lightgrey')
plt.ylabel('Number of Confirmed Cases', size=12)
plt.title('States with maximum confirmed cases', size=16)
plt.show()

#Statewise number of deaths from Covid-19 in India
Mydf = Mydf.sort_values(by=['Deaths'], ascending=False)
plt.figure(figsize=(12, 8), dpi=80)
plt.bar(Mydf['State'][:5],
        Mydf['Deaths'][:5], align='center', color='lightgrey')
plt.ylabel('Number of Deaths', size=12)
plt.title('States with maximum deaths', size=16)
plt.show()

#Statewise ratio of confirmed cases per population
Mydf['Confirmed/Population'] = (Mydf['Confirmed']/Mydf['Population']).round(2)
Mydf = Mydf.sort_values(by=['Confirmed/Population'], ascending=False)
plt.figure(figsize=(12, 8), dpi=80)
plt.bar(Mydf['State'][:5],
        Mydf['Confirmed/Population'][:5], align='center', color='lightgrey')
plt.ylabel('Confirmed/Population', size=12)
plt.title('States with max Confirmed/Population ratio', size=16)
plt.show()
