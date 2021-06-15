#!/usr/bin/env python
# coding: utf-8

# In[77]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter


# In[2]:


import sys
# get_ipython().system('{sys.executable} -m pip install matplotlib')


# In[3]:


df = pd.read_csv('/users/apple/Desktop/Data Analysis/data/survey_results_public.csv')


# In[4]:


coutries = ['Poland']
filt = (df['Country'].isin(coutries)) & (df['ConvertedComp'] > 70000) & df['LanguageWorkedWith'].str.contains('Python', na=False)
df.loc[filt, ['Country', 'LanguageWorkedWith', 'ConvertedComp']]


# In[ ]:





# In[5]:


df['LanguageWorkedWith'].str.split(";")


# In[54]:


# for el in df['LanguageWorkedWith'].str.split(";"):


# In[87]:


unique_list = []   
# traverse for all elements
All_lang = [ el for el in df['LanguageWorkedWith'].str.split(";")]
for el in All_lang:
    if type(el) != float:
        for i in el:
            if i not in unique_list and type(i) == str:
                unique_list.append(i)
# print(unique_list)

lan = dict.fromkeys(unique_list, 0)

for el in All_lang:
    if type(el) != float:
        for i in el:
            lan[i] += 1
# print(lan)


# In[108]:


pos = np.arange(len(lan.keys()))
width = 0.8
ax = plt.axes()
ax.set_xticks(pos + (width / 2))
ax.set_xticklabels(lan.keys())

plt.bar(lan.keys(), lan.values(), width, color='g')
plt.setp(ax.get_xticklabels(), rotation=60, horizontalalignment='right')
plt.title("Statistics of programming languages in Poland 2019")
plt.ylabel("Number of pople")
plt.savefig('Stats_2019.jpg', format = 'jpg')
plt.tight_layout()
plt.show()


