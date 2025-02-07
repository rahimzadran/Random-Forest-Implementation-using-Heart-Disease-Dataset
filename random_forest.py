# -*- coding: utf-8 -*-
"""Random Forest

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LQKVKhpre2AYPdY6dC6GyUmPwql_1jU3

# 1. Load the Dataset:
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler
Scalar = StandardScaler()

df = pd.read_csv('heart.csv')

df.head()

"""# 2. Check for Missing Values:"""

missing_values = df.isnull().sum()
print(missing_values)

"""## Checking the Columns Types"""

#Numeric Columns
numerical_columns = df.select_dtypes(include=['number']).columns
print(numerical_columns)

# Categorical Columns
categorical_columns = df.select_dtypes(include=['object']).columns
print(categorical_columns)

df['Sex'] = df['Sex'].map({'M':1,'F':0})
df['ExerciseAngina'] = df['ExerciseAngina'].map({'Y':1,'N':0})

df = pd.get_dummies(df, columns=['ChestPainType', 'RestingECG', 'ST_Slope'], drop_first=True)

df.head()

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df[['Age', 'RestingBP', 'Cholesterol', 'FastingBS', 'MaxHR', 'Oldpeak']] = scaler.fit_transform(df[['Age', 'RestingBP', 'Cholesterol', 'FastingBS', 'MaxHR', 'Oldpeak']])

df.head()

import seaborn as sns
import matplotlib.pyplot as plt

# Calculate the correlation matrix, only including numerical features
correlation_matrix = df.corr(numeric_only=True)

# Plot the correlation matrix using seaborn heatmap
plt.figure(figsize=(10, 8))  # Adjust the size of the plot
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)

# Show the plot
plt.title('Correlation Matrix')
plt.show()

from sklearn.model_selection import train_test_split

X = df.drop('HeartDisease', axis=1)  # Features
y = df['HeartDisease']  # Target variable

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import LabelEncoder
import numpy as np

rf_model = RandomForestClassifier(n_estimators=100, random_state=42)

# Now, try fitting the model again
rf_model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = rf_model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

# Print results
print(f"Accuracy: {accuracy:.2f}")
print("Confusion Matrix:")
print(conf_matrix)
print("Classification Report:")
print(class_report)