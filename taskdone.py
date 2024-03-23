# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wtnc-fG6spB5xZt4UR9KNrucMHfZLvGi
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/content/transactions.csv')

df

list(df.columns)

df.head(15)

unique_types = df['type'].unique()

print("Unique Transaction Types:")
print(unique_types)

top_destinations = df['nameDest'].value_counts().head(10)

print("Top 10 Transaction Destinations with Frequencies:")
print(top_destinations)

fraudulent_transactions = df[df['isFraud'] == 1]

print("Rows where fraud was detected:")
print(fraudulent_transactions)

transaction_type_counts = df['type'].value_counts()
plt.figure(figsize=(10, 6))
transaction_type_counts.plot(kind='bar', color='skyblue')
plt.title('Transaction Type Bar Chart')
plt.xlabel('Transaction Type')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.show()

fraud_transaction_counts = df[df['isFraud'] == 1]['type'].value_counts()
plt.figure(figsize=(10, 6))
fraud_transaction_counts.plot(kind='bar', color='salmon')
plt.title('Transaction Types Split by Fraud Bar Chart')
plt.xlabel('Transaction Type')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.show()

description = ("While the transaction frequencies depend on the whims of the available data, what is interesting here is that fraudulent "
               "activity is only seen on CASH_OUT and TRANSFER transactions. This insight informs management to focus the effort of manual "
               "reviews which could result in less fraud being missed.")

print(description)

distinct_destinations_per_source = df.groupby('nameOrig')['nameDest'].nunique()

distinct_destinations_per_source_sorted = distinct_destinations_per_source.sort_values(ascending=False)

result_df = pd.DataFrame({'nameOrig': distinct_destinations_per_source_sorted.index, 'DistinctDestinations': distinct_destinations_per_source_sorted.values})

print("DataFrame with the number of distinct destinations each source has interacted with:")
print(result_df)