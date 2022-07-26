#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[6]:


simpsons = pd.read_html("https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes")


# In[7]:


len(simpsons)


# In[10]:


simpsons[4]


# In[ ]:




