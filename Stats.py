#!/usr/bin/env python
# coding: utf-8

# In[37]:


import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as seaborn
import scipy.stats as stats


# In[3]:


#read data set
df = pd.read_csv('Data.csv')
#print first 5 rows
df.head()


# In[4]:


#calculate mean times for each step
cols = ['start program','setup program', 'run program','end program']
means = df[cols].mean()
std = df[cols].std()
means
std


# In[5]:


#overall descriptive statistics
descriptive = df.describe().round(2)
descriptive


# In[67]:


#compare two different pro
average_times = df.groupby('program')['total time']
ax = average_times.plot.kde()
std_p = lambda x: np.std(x, ddof=0)

average_times = average_times.agg([np.mean, std_p])
average_times.columns = ['average_time', 'std_deviation']
average_times.style.format('{:.3f}')


# In[64]:


histogram = df.plot.hist(column=["total time"], by="program",bins=6, alpha=0.5,figsize=(10, 8))
df.plot(x="total time", y=["errors"])
plt.show


# In[52]:


plt.plot(df["total time"], df["clicks"])


# In[53]:


seaborn.scatterplot(df["errors"])


# In[56]:


sns.boxplot(df['total time'] )


# In[30]:






# In[ ]:




