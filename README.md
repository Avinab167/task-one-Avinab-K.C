#  Retail Store Sales Data Analysis

##  Project Overview

This project demonstrates a complete data analysis workflow using Python (Pandas) and Power BI. The objective was to clean, preprocess, and visualize retail store sales data to generate meaningful business insights.

The project covers:

- Data Cleaning
- Missing Value Treatment
- Data Type Conversion
- Data Validation
- Power BI Dashboard Development
- Business Insight Generation

---

##  Dataset Information

The dataset contains transaction-level retail sales data with the following fields:

| Column Name | Description |
|------------|-------------|
| Transaction Date | Date of transaction |
| Item | Product name |
| Price Per Unit | Unit price of product |
| Quantity | Number of units purchased |
| Total Spent | Total transaction amount |
| Discount Applied | Whether discount was applied |

---

##  Technologies Used

- Python
- Pandas
- NumPy
- Power BI
- Jupyter Notebook

---

##  Data Cleaning & Preprocessing

### 1. Data Exploration

The dataset was examined using:

```python
df.head()
df.info()
df.shape
```

### 2. Missing Value Handling

| Column | Treatment |
|----------|-----------|
| Item | Filled with "Unknown" |
| Price Per Unit | Median Imputation |
| Quantity | Median Imputation |
| Total Spent | Median Imputation |
| Discount Applied | Mode Imputation |

### 3. Duplicate Check

```python
df.duplicated().sum()
```

No duplicate records were identified.

### 4. Data Type Conversion

#### Transaction Date

```python
pd.to_datetime(df['Transaction Date'], dayfirst=True)
```

#### Discount Applied

```python
df['Discount Applied'].astype(bool)
```

---

##  Power BI Dashboard

The cleaned dataset was imported into Power BI to create interactive visualizations.

### Dashboard Components

###  Sales Over Time

- Tracks sales trends
- Identifies peak sales periods
- Detects seasonality patterns

###  Top Products

- Best-selling products by revenue
- Best-selling products by quantity

###  Discount Impact Analysis

- Discount vs Non-discount sales comparison
- Promotion effectiveness evaluation

###  Price Distribution

- Product price spread analysis
- Identification of pricing patterns

###  KPI Cards

- Total Revenue
- Average Transaction Value
- Discount Percentage

---

##  Key Insights

### Sales Trends

- Identified customer purchasing patterns over time.
- Revealed opportunities for inventory planning.

### Product Performance

- Highlighted products driving the highest revenue.
- Identified slow-moving inventory.

### Discount Effectiveness

- Measured impact of promotional campaigns.
- Compared discounted and regular-price transactions.

### Revenue Analysis

- Evaluated transaction values and revenue contribution.
- Supported business decision-making with data-driven metrics.

---

##  Project Structure

```text
Retail-Store-Sales-Analysis/
│
├── data/
│   ├── retail_store_sales.csv
│   └── retail_store_sales_cleaned.csv
│
├── notebooks/
│   └── data_cleaning_analysis.ipynb
│
├── powerbi/
│   └── Retail_Sales_Dashboard.pbix
│
├── report/
│   └── Task-1-Avinab-KC-Report.pdf
│
└── README.md
```

---

##  How to Run

### Clone Repository

```bash
git clone https://github.com/yourusername/retail-store-sales-analysis.git
```

### Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn
```

### Run Analysis

```bash
python retail_sales_analysis.py
```

---

##  Future Improvements

- Automated data validation pipeline
- Advanced imputation techniques (KNN, Iterative Imputation)
- Real-time dashboard refresh
- KPI alert system
- Enhanced customer segmentation analysis

---

##  Author

**Avinab K.C**

Data Analytics Internship Project – DecodeLabs

---

##  License

This project is created for educational and internship purposes.