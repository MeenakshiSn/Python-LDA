# -*- coding: utf-8 -*-
"""Untitled177.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WuYRLJ6IsWdVSy6R-dq5IGNZwjG9vmIB

#**Linear Discriminant Analysis (LDA)**

- Supervised ML Dimensionality reduction tech
- used for classification data
- helps is minimizing the variance within same class and maximizing the mean between separate classes
- solves the problem of overlapping from logistic regression
"""



"""**importing the libraries**"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""**import the dataset**"""

from sklearn.datasets import load_digits
digits = load_digits()
digits

x = pd.DataFrame(digits.data, columns = digits.feature_names)
y = pd.DataFrame(digits.target, columns = ['target'])

x.shape

y.shape

x.head()

y.head()

"""**StandardScaler**"""

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

x_std = sc.fit_transform(x)
x_std

"""**Total Classes in target**"""

y['target'].nunique()

"""**Train Test Split**"""

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x_std, y, test_size=0.2, random_state=42)

"""**Apply LDA**

n_components = 10-1 = 9

Maximum value of components = total classes in target - 1

Range of n_components = (1, total classes in target-1)

"""

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

lda = LinearDiscriminantAnalysis(n_components = 9)
lda.fit(x_train, y_train)

"""**Making Predictions**"""

y_pred = lda.predict(x_test)
y_pred

"""**Evaluate model**"""

from sklearn.metrics import accuracy_score, classification_report

print(accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

