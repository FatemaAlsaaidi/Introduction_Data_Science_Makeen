#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
import csv
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("ass4.csv")


# In[18]:


#Resoluation of data
sns.lineplot(x="Year", y="Number of Births", data=df)

plt.show()


# In[19]:


#Visualize the data
sns.set(rc={'figure.figsize':(30,30)})
sns.boxplot(data=df)
plt.semilogy()


# In[20]:


#Visualize the data
sns.pairplot(df)


# In[21]:


#Aggregated of data
grouped = df.groupby("Education Level of Mother")

aggregated = grouped["Number of Births"].sum()
print(aggregated)


# In[22]:


#Description of data
description = df["Number of Births"].describe()

print(description)


# In[23]:


import numpy as np

# Generate a list of 1000 random integers between 1 and 100000
random_integers = np.random.randint(1, 100000, 1000)

# Calculate the mean and standard deviation of the list of random integers
mean = np.mean(random_integers)
std = np.std(random_integers)

# Calculate the z-scores
z_scores = np.abs(random_integers - mean) / std

# Print the z-scores
#print(z_scores)
sns.boxplot(data=df)
plt.semilogy()

# Identify the outliers
outliers = np.where(z_scores > 1.5)

# Print the outliers
print("Outliers is",outliers)


# In[24]:


# Generate a list of 10 random integers between 1 and 100
random_integers = np.random.randint(1, 100, 10)

# Add a new column to the DataFrame with the standardized values
df["standardized"] = df["Number of Births"] - df["Number of Births"].mean() / df["Number of Births"].std()

# Add a new column to the DataFrame with the normalized values
df["normalized"] = df["Number of Births"] / df["Number of Births"].max()

# Print the DataFrame with the standardized and normalized values
print(df)


# In[34]:


m = pd.DataFrame(np.random.randint(1, 100, size= (100,2)), columns=list('xy'))
print(m.head())

plt.scatter(m['x'], m['y'])
plt.show()


# In[ ]:




