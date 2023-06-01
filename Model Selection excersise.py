#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("dataset.csv")


# In[11]:


def mean_squared_error(true_values, predicted_values):
  """Calculates the mean squared error between two arrays.

  Args:
    true_values: The ground truth values.
    predicted_values: The predicted values.

  Returns:
    The mean squared error.
  """

  difference = true_values - predicted_values
  squared_difference = np.square(difference)
  mean_squared_error = np.mean(squared_difference)

  return mean_squared_error

# Load the CSV file into a NumPy array
true_values = np.loadtxt('dataset.csv', delimiter=',', skiprows=1, usecols=1)
predicted_values = np.loadtxt('dataset.csv', delimiter=',', skiprows=1, usecols=2)

# Calculate the MSE
mse = mean_squared_error(true_values, predicted_values)

print(mse)


# In[12]:


# Calculate the accuracy as 1 - MSE
accuracy = 1 - mse

# Calculate the error rate as MSE / 100
error_rate = mse / 100

print('Accuracy:', accuracy)
print('Error rate:', error_rate)


# In[ ]:




