#Covid 19 Visualization

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
        
#This includes analysis of country wise and day wise covid 19 active cases, recovered, deaths and total number of cases.
#Reading the necessary data and exploring the first five dataset values

country_wise = pd.read_csv("../input/corona-virus-report/country_wise_latest.csv")
day_wise = pd.read_csv("../input/corona-virus-report/day_wise.csv")
country_wise.head()
day_wise.head()
#Using seaborn let's analyze the scenario

import seaborn as sns
country_categorical = country_wise[['Confirmed','Recovered','Active','Deaths']]
sns.lineplot(data = country_categorical)
day_categorical = day_wise[['Confirmed','Recovered','Active','Deaths']]
sns.lineplot(data = day_categorical)
sns.kdeplot(data = country_wise['New deaths'],shade = True)
sns.kdeplot(data = day_wise['New deaths'],shade = True)
sns.heatmap(data = day_wise[['New cases','New deaths','New recovered']])
sns.jointplot(x = country_wise['Active'],y = day_wise['Active'],kind = 'kde')
