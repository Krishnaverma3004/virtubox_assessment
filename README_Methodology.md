# Data Analyst Assessment — Online Retail

Dataset: UCI Online Retail  
Source: https://archive.ics.uci.edu/dataset/352/online+retail

## Package structure
- `Data_Analyst_Assessment_Q1-Q10.xlsx` — completed written answers and analysis tables.
- `Processed_Data.csv` — analysis-ready transaction data for direct import into Google Sheets as **Processed Data**.
- `Online Retail.xlsx` — the original supplied raw data; use it as the **Data** worksheet.
- `Data_Analyst_Management_Presentation.pptx` — 7-slide management presentation.
- `management_dashboard_static.png` — dashboard reference image.
- `analysis.py` — reproducible Python/Pandas processing script.
- PNG files — supporting charts.

## Key figures
- Raw rows: 541,909
- Processed positive-sales rows: 524,878
- Gross sales revenue: £10,642,110.80
- Cancellation value: £893,979.73 (8.4% of gross sales)
- Repeat-customer revenue share among identified customers: 93.1%
- UK revenue share: 84.6%
- International AOV vs UK: 1.69×
- Sep–Nov share of gross sales: 34.9%

## Important limitations
CustomerID is missing for many raw rows; customer metrics therefore cover identifiable customers only. December 2011 is partial through 09-Dec-2011. The dataset has no cost/margin field, so profitability cannot safely be concluded.

## Google Sheets / Looker Studio
1. Upload `Online Retail.xlsx` to Google Sheets and rename its data tab to `Data`.
2. Import `Processed_Data.csv` as a new tab named `Processed Data`.
3. Copy the Q1–Q10 answer sheets and analysis tables from the completed workbook into the same Google Sheet.
4. Build the Looker Studio dashboard using `Monthly_Analysis`, `Country_Analysis`, `Product_Analysis`, `Customer_Summary`, and `Cancellation_Analysis`.
5. Publish/share the Looker Studio report and paste its URL into the `Q8_Dashboard` worksheet.
