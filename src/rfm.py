import datetime as dt

def create_rfm(df):
    print("Creating RFM...")

    snapshot_date = df['InvoiceDate'].max() + dt.timedelta(days=1)

    rfm = df.groupby('Customer ID').agg({
        'InvoiceDate': lambda x: (snapshot_date - x.max()).days,
        'Invoice': 'count',
        'TotalPrice': 'sum'
    })

    rfm.columns = ['Recency', 'Frequency', 'Monetary']

    rfm = rfm.reset_index()

    print("RFM created")

    return rfm