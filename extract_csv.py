#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd

# reading csv file from the website
df_premere21 = pd.read_csv('https://www.football-data.co.uk/mmz4281/2122/E0.csv')


# In[6]:


# show the dataframe
df_premere21


# In[9]:


# rename columns
df_premere21.rename(columns= {'FTHG': 'home_goals',
                              'FTAG': 'away_goals'}, inplace = True)
# show dataframe
df_premere21


# In[ ]:




