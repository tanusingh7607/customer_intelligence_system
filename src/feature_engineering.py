import pandas as pd

def feature_engineering(df):
    print("Engineering features...")

    # Total price
    df['TotalPrice'] = df['Quantity'] * df['Price']

    # Convert date
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], errors='coerce')

    # Extract features
    df['Month'] = df['InvoiceDate'].dt.month
    df['Day'] = df['InvoiceDate'].dt.day

    # Avg order value
    df['AvgOrderValue'] = df['TotalPrice'] / df['Quantity']

    print("Features added")

    return df