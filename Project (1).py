#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

import os
print(os.listdir("C:"))


# In[6]:


df=pd.read_csv("C:/2015.csv")
df.head()


# In[7]:


df.info


# In[8]:


df.describe()


# In[9]:


df.info()


# In[10]:


df.corr()


# In[11]:


sns.heatmap(df.corr())


# In[12]:


plt.hist(df["Generosity"],bins=50,color='red')

plt.xlabel("Generosity")
plt.ylabel("Value")
plt.title("Histogram")
plt.show()


# In[13]:


y=df["Economy (GDP per Capita)"]
x=df["Happiness Score"]
plt.scatter(x,y)
plt.figure(figsize=(40,40))
plt.show()


# In[14]:


print(df["Happiness Score"]>7)


# In[15]:


x=df["Happiness Score"]>7
print(df[x])


# In[16]:


print(df[x].head())


# In[17]:


y=((df["Happiness Score"]<5) & (df["Freedom"]>0.35))
print(y)


# In[18]:


print(df[y])


# In[19]:


z=df.groupby("Region")


# In[20]:


print(z.get_group("Western Europe"))


# In[21]:


k=z.get_group("Western Europe")
print("Mean Score of Western Europe is :"+ str(k["Happiness Score"].mean()))


# In[22]:


z.count()


# In[27]:


l=0
for i in (df["Region"].unique()):
    print("Mean Happiness Score of",end=' ')
    print(i,"is",end=' ')
    k=z.get_group(i)
    print(k["Happiness Score"].mean())
    if (k["Happiness Score"].mean())>l:
        l=k["Happiness Score"].mean()
        m=i


# In[29]:


print ("The Happiest Region is " + m + " with Happiness Score of " + str (l))


# In[32]:


def display_country(country):
    for j in df["Country"]:
        if j==country:
            v1=j.index
            for n in range(13):
                  print(df.iloc[v1,n],end=" ")
country=input("Enter the Name of the country")
display_country(country)


# In[ ]:




