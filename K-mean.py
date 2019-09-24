#!/usr/bin/env python
# coding: utf-8
K - mean 클러스터링
# # k - mean steps
# ## 1. Prepare dfata
# ## 2. decide how many clusters you need
# ## 3. choose initial center of cluster(centroid)
# ### randomly select centroid
# ### manually assign centroid
# ### kmean ++
# ## 4. assign data point to nearest cluster
# ## 5. move centroid to ther center of its cluster
# ## repeat step 4 and step 5
#  ### unyil there is no assigned cluster change

# In[3]:


import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().magic(u'matplotlib inline')


# create data points

# In[4]:


df = pd.DataFrame(columns=['x', 'y'])


# In[5]:


df.loc[0] = [3,1]
df.loc[1] = [4,1]
df.loc[2] = [3,2]
df.loc[3] = [4,2]
df.loc[4] = [10,5]
df.loc[5] = [10,6]
df.loc[6] = [11,5]
df.loc[7] = [11,6]
df.loc[8] = [15,1]
df.loc[9] = [15,2]
df.loc[10] = [16,1]
df.loc[10] = [16,2]


# In[6]:


df.head(20)


# ## Visualize data points on 2D plot

# In[7]:


# visualize data point
sns.lmplot('x', 'y', data=df, fit_reg=False, scatter_kws={'s': 200}) # x-axis, y-axis, data, ni lune, maker size

# title
plt.title('kean plot')

# x-axis label
plt.xlabel('x')

#y-axis label
plt.ylabel('y')


# K-mean clustering

# In[8]:


# convert dataframe to numpy array
data_points = df.values


# In[9]:


kmeans = KMeans(n_clusters=3).fit(data_points)


# In[10]:


# cluster id for each data point
kmeans.labels_


# In[11]:


# this is final controids postion
kmeans.cluster_centers_


# In[12]:


df['cluster_id'] = kmeans.labels_


# In[13]:


df.head(12)


# In[17]:


sns.lmplot('x', 'y', data=df, fit_reg=False, # X-axis, Y-axis, data, no line 
         scatter_kws={"s": 150},
          hue="cluster_id") # color


#title
plt.title('after kmean clustering')


# In[ ]:




