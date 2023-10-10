#!/usr/bin/env python
# coding: utf-8



import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.simplefilter("ignore")
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

#parameters

c = 1.0
output_file = 'model_C=%s.bin' % c

#data_prepration
print("Reading the data")
df = pd.read_csv("insurance_pred/train.csv")
df.head()

del df['id'] 

df.isnull()


df['Gender'] = df['Gender'].map({'Male': 1, 'Female': 2})



df.Vehicle_Age.unique()
df['Vehicle_Age'] = df['Vehicle_Age'].map({'> 2 Years': 1, '1-2 Year': 2, '< 1 Year': 3})


# In[6]:


df.Vehicle_Damage.unique()
df['Vehicle_Damage'] = df['Vehicle_Damage'].map({'Yes': 1, 'No': 2})


# In[7]:


df.Response.value_counts(normalize=True)


X = df.drop("Response", axis=1)
#X = df.drop("id", axis=1)

X.head()

# y data
y = df["Response"]
y.head()


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
X_test, X_val, y_test, y_val = train_test_split(X_train, y_train, test_size=0.5, random_state=1)

X_train


scaler = StandardScaler()
df_train = scaler.fit_transform(X_train)
df_val = scaler.transform(X_val)
df_test = scaler.transform(X_test)



print("training the model")
lr = LogisticRegression()

lr.fit(X_train, y_train)


LogisticRegressionScore = lr.score(X_val, y_val)
print("Accuracy obtained by Logistic Regression model:",LogisticRegressionScore*100)



LogisticRegressionScore = lr.score(X_test, y_test)
print("Accuracy obtained by Logistic Regression model:",LogisticRegressionScore*100)



LogisticRegressionScore = lr.score(X_train, y_train)
print("Accuracy obtained by Logistic Regression model:",LogisticRegressionScore*100)


output_file



with open(output_file, 'wb') as f_out:
    pickle.dump((scaler,lr), f_out)


print(f'the model is saved to {output_file}')   