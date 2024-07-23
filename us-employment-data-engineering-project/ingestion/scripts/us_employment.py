#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[13]:


df = pd.DataFrame(pd.read_excel("/home/aham/us-employment/ingestion/data/laucnty05.xlsx"))


# In[14]:


df.drop(index=df.index[:5], axis=0, inplace=True)


# In[15]:


df.drop(index=df.tail(3).index,axis = 0, inplace=True)


# In[16]:


df.drop(columns="Unnamed: 5", inplace=True)


# In[17]:


df.replace(to_replace="N.A.", value=0, inplace=True)


# In[18]:


df.columns = ["LAUS_code", "state_fips", "county_fips", "county_state", "year", "labor_force", "employed", "unemployed", "unemployment_rate"]


# In[19]:


df['fips'] = df['state_fips'] + df['county_fips']


# In[20]:


df


# In[21]:


print(pd.io.sql.get_schema(df, "us_employment_data"))


# In[22]:


df.year = pd.to_numeric(df.year)
df.unemployment_rate = pd.to_numeric(df.unemployment_rate)


# In[23]:


print(pd.io.sql.get_schema(df, "us_employment_data"))


# In[13]:


df.to_csv(f"/home/aham/us-employment/ingestion/data/us_employment_{df.year[6]}.csv", index=None, header=True)


# In[14]:


df_csv = pd.DataFrame(pd.read_csv(f"/home/aham/us-employment/ingestion/data/us_employment_{df.year[6]}.csv"))


# In[15]:


df_csv

