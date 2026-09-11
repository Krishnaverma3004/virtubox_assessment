import pandas as pd

INPUT = "Online Retail.xlsx"

raw = pd.read_excel(INPUT)
df = raw.drop_duplicates().copy()

for c in ["InvoiceNo", "StockCode", "Description", "Country"]:
    df[c] = df[c].astype("string").str.strip().str.replace(r"\s+", " ", regex=True)

df["CustomerID"] = df["CustomerID"].astype("Int64")
df["Revenue"] = df["Quantity"] * df["UnitPrice"]
df["IsCancellation"] = df["InvoiceNo"].str.upper().str.startswith("C") | (df["Quantity"] < 0)

sales = df[
    (df["Quantity"] > 0) &
    (df["UnitPrice"] > 0) &
    (df["Description"].notna())
].copy()

sales["Month"] = sales["InvoiceDate"].dt.to_period("M").astype(str)
sales["Year"] = sales["InvoiceDate"].dt.year
sales["Quarter"] = sales["InvoiceDate"].dt.to_period("Q").astype(str)
sales["DayOfWeek"] = sales["InvoiceDate"].dt.day_name()
sales["Hour"] = sales["InvoiceDate"].dt.hour

monthly = sales.groupby("Month").agg(
    Revenue=("Revenue", "sum"),
    Orders=("InvoiceNo", "nunique"),
    Units=("Quantity", "sum"),
    Customers=("CustomerID", "nunique")
).reset_index()

country = sales.groupby("Country").agg(
    Revenue=("Revenue", "sum"),
    Orders=("InvoiceNo", "nunique"),
    Customers=("CustomerID", "nunique"),
    Units=("Quantity", "sum")
).sort_values("Revenue", ascending=False)

customer = sales[sales["CustomerID"].notna()].groupby("CustomerID").agg(
    Revenue=("Revenue", "sum"),
    Orders=("InvoiceNo", "nunique"),
    Units=("Quantity", "sum")
).sort_values("Revenue", ascending=False)

cancellations = df[df["InvoiceNo"].str.upper().str.startswith("C")].copy()
cancellations["CancellationValue"] = -(cancellations["Quantity"] * cancellations["UnitPrice"])

print("Raw rows:", len(raw))
print("Exact duplicates:", raw.duplicated().sum())
print("Processed sales rows:", len(sales))
print("Gross sales revenue:", round(sales["Revenue"].sum(), 2))
print("Cancellation value:", round(cancellations["CancellationValue"].sum(), 2))
