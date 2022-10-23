#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt


# In[3]:


def get_csv(web_link):
    return pd.read_csv(web_link)


# In[4]:


df = get_csv(r'https://raw.githubusercontent.com/odonnell31/NBA-Team-Strategies/main/data/nba_teams_data_1990_2020.csv')


# In[5]:


print(df.head())


# In[16]:


losing_data = df.groupby("Team")[["Losing_season", "Finals_Team"]].agg("sum")


# In[17]:


losing_data


# In[18]:


losing_data.sort_values(by = "Losing_season", ascending = False)


# In[19]:


losing_data = losing_data.sort_values(by = "Losing_season", ascending = True)

x = losing_data.index
y = losing_data["Losing_season"]

plt.figure(figsize = (5, 10))
plt.barh(x, y, color = "maroon")
plt.title("Number of Losing Seasons from 1990-2020 by Team")
plt.xlabel("Number of Seasons")
plt.ylabel("NBA Team")
plt.show()


# In[ ]:




