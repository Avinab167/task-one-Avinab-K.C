import pandas as pd


#loading the dataset
df = pd.read_csv("retail_store_sales.csv") 


#checking the basic information about the dataset
df.head()
df.info()
print(df.shape)


#checking for missing values
df.isnull().sum()

#checking for duplicates
print(df.duplicated().sum())


#filling missing values in the 'Item' column with 'Unknown'
df['Item'] = df['Item'].fillna('Unknown')


#filling missing values
df['Price Per Unit'] = df['Price Per Unit'].fillna(df['Price Per Unit'].median())
df['Quantity'] = df['Quantity'].fillna(df['Quantity'].median())
df['Total Spent'] = df['Total Spent'].fillna(df['Total Spent'].median())
mode_value = df['Discount Applied'].mode()[0]
df['Discount Applied'] = df['Discount Applied'].fillna(mode_value)


#checking for missing values after filling
print(df.isnull().sum())


#converting 'Transaction Date' to datetime format
df['Transaction Date'] = pd.to_datetime(
    df['Transaction Date'],
    dayfirst=True
)

print(df['Transaction Date'].dtype)


#converting 'Discount Applied' to boolean
df['Discount Applied'] = df['Discount Applied'].astype(bool)


#checking the data types of the columns
print(df.dtypes)


#final summary of the dataset
print("Shape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())


#saving the cleaned dataset to a new CSV file
df.to_csv("retail_store_sales_cleaned.csv", index=False)