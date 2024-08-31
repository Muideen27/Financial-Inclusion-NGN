#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install pyreadstat pandas nbformat')


# In[3]:


import pandas as pd
import pyreadstat
import nbformat as nbf

# Load the dataset from .sav file
file_path = "C:\\Users\\Open User\\Downloads\\A2F-2023-Survey-Dataset-for-publishing\\A2F-2023-Survey-Dataset-for-publishing.sav"
df, meta = pyreadstat.read_sav(file_path)


# In[4]:


# Display the first few rows of the DataFrame
print(df.head())


# In[9]:


df.to_csv("data.csv")


# In[10]:


df=pd.read_csv("data.csv", low_memory=False)


# In[11]:


print(df.head())


# In[12]:


# Count the number of duplicate rows
num_duplicates = df.duplicated().sum()
print(f"Number of duplicate rows: {num_duplicates}")


# In[18]:


# Calculate the percentage of missing data for each column
missing_percentages = df.isna().mean()

# Filter columns with less than 5% missing data
columns_less_than_5_percent = missing_percentages[missing_percentages < 0.05].index
num_columns_less_than_5_percent = len(columns_less_than_5_percent)

print(f"Number of columns with less than 5% missing data: {num_columns_less_than_5_percent}")


# In[19]:


# For rows, calculate the percentage of missing data for each row
row_missing_percentages = df.isna().mean(axis=1)

# Filter rows with less than 5% missing data
rows_less_than_5_percent = row_missing_percentages[row_missing_percentages < 0.05].index
num_rows_less_than_5_percent = len(rows_less_than_5_percent)

print(f"Number of rows with less than 5% missing data: {num_rows_less_than_5_percent}")


# In[20]:


# Define the threshold for missing data (e.g., 5%)
threshold = 0.05

# Calculate the percentage of missing data for each column
missing_percentages = df.isna().mean()

# Identify columns that have more than the threshold percentage of missing data
columns_to_drop = missing_percentages[missing_percentages > threshold].index

# Drop those columns from the DataFrame
df_cleaned = df.drop(columns=columns_to_drop)


# In[22]:


# Display the number of columns before and after cleaning
print(f"Original number of columns: {df.shape[1]}")
print(f"Number of columns after removing those with >{threshold*100}% missing data: {df_cleaned.shape[1]}")


# In[23]:


# Saving the cleaned DataFrame to a new CSV file
df_cleaned.to_csv("data_cleaned.csv", index=False)


# In[13]:


# Check if there are still any missing values in the cleaned DataFrame
missing_values_after_filter = df_cleaned.isna().sum().sum()

if missing_values_after_filter > 0:
    print(f"There are still {missing_values_after_filter} missing values in the DataFrame after applying the 5% filter.")
else:
    print("There are no missing values left in the DataFrame after applying the 5% filter.")


# In[24]:


# Fill missing values with the mean for numeric columns
numeric_columns = df_cleaned.select_dtypes(include=['number']).columns
df_cleaned[numeric_columns] = df_cleaned[numeric_columns].fillna(df_cleaned[numeric_columns].mean())


# In[25]:


# For categorical columns, fill with the mode (most frequent value)
categorical_columns = df_cleaned.select_dtypes(include=['object']).columns
for column in categorical_columns:
    df_cleaned[column] = df_cleaned[column].fillna(df_cleaned[column].mode()[0])


# In[26]:


# Check if there are still any missing values
missing_values_after_imputation = df_cleaned.isna().sum().sum()

if missing_values_after_imputation > 0:
    print(f"There are still {missing_values_after_imputation} missing values in the DataFrame after simple imputation.")
else:
    print("There are no missing values left in the DataFrame after simple imputation.")


# In[27]:


# Save the cleaned DataFrame to a CSV file
output_file_path = "cleaned_data.csv"
df_cleaned.to_csv(output_file_path, index=False)

print(f"Cleaned DataFrame has been saved to {output_file_path}.")


# In[28]:


print(df_cleaned.info())


# In[29]:


print(df_cleaned.head())


# In[ ]:





# In[ ]:





# In[ ]:




