# Streamlit Application generated from supermarket_sales.ipynb
import streamlit as st

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Load the dataset
data = pd.read_csv('supermarket_sales.csv')

# Display the first few rows of the dataset
print(data.head())

## Exploratory Data Analysis (EDA)
# Check for missing values
print(data.isnull().sum())

# Basic statistics of numerical features
print(data.describe())

# Visualizing the distribution of 'Total' sales
plt.figure(figsize=(10, 6))
sns.histplot(data['Total'], bins=30, kde=True)
plt.title('Distribution of Total Sales')
plt.xlabel('Total Sales')
plt.ylabel('Frequency')
plt.show()

# Countplot for 'Gender'
plt.figure(figsize=(8, 5))
sns.countplot(x='Gender', data=data)
plt.title('Count of Customers by Gender')
plt.show()

# Boxplot for 'Total' sales by 'Product line'
plt.figure(figsize=(12, 6))
sns.boxplot(x='Product line', y='Total', data=data)
plt.title('Total Sales by Product Line')
plt.xticks(rotation=45)
plt.show()

## Data Preparation
# Convert categorical variables to numeric using one-hot encoding
data_encoded = pd.get_dummies(data, columns=['Branch', 'City', 'Customer type', 'Gender', 'Product line', 'Payment'], drop_first=True)

# Define features and target variable for classification
X = data_encoded.drop(['Invoice ID', 'Date', 'Time', 'Total'], axis=1)
y = (data['Total'] > data['Total'].mean()).astype(int)  # Binary classification: above or below average total sales

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

## Modeling without Data Preparation (using raw data)
# Using Random Forest Classifier without any preparation (just for demonstration)
model_raw = RandomForestClassifier(random_state=42)
model_raw.fit(X_train, y_train)

# Predictions and evaluation
y_pred_raw = model_raw.predict(X_test)
print("Classification Report (Raw Data):")
print(classification_report(y_test, y_pred_raw))
print("Confusion Matrix (Raw Data):")
print(confusion_matrix(y_test, y_pred_raw))

## Modeling with Data Preparation (using prepared data)
model_prepared = RandomForestClassifier(random_state=42)
model_prepared.fit(X_train, y_train)

# Predictions and evaluation
y_pred_prepared = model_prepared.predict(X_test)
print("Classification Report (Prepared Data):")
print(classification_report(y_test, y_pred_prepared))
print("Confusion Matrix (Prepared Data):")
print(confusion_matrix(y_test, y_pred_prepared))

# Data correlation analysis
# Convert categorical variables to numeric using one-hot encoding
data_encoded = pd.get_dummies(data, columns=['Branch', 'City', 'Customer type', 'Gender', 'Product line', 'Payment'], drop_first=True)

# Data correlation analysis
# Convert categorical variables to numeric using one-hot encoding
data_encoded = pd.get_dummies(data, columns=['Branch', 'City', 'Customer type', 'Gender', 'Product line', 'Payment'], drop_first=True)

numerical_data = data_encoded.select_dtypes(include=['number'])  # Select only numerical columns
correlation_matrix = numerical_data.drop(columns=['Invoice ID', 'Date'], errors='ignore').corr()  # errors='ignore' to handle if columns are already dropped

# Set up the matplotlib figure
plt.figure(figsize=(12, 8))

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True, cbar_kws={"shrink": .8})

