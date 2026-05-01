import pandas as pd

def load_data(path):
    print("Loading data...")
    df = pd.read_excel('..\data\online_retail_II.xlsx')
    print("Loaded", df.shape[0], "records")
    return df

def clean_data(df):
    print("Cleaning data...")

    #column names
    df.columns = df.columns.str.strip()

    # Remove missing Customer ID
    df = df.dropna(subset=['Customer ID'])

    # Remove cancelled orders
    df = df[~df['Invoice'].astype(str).str.startswith('C')]

    # Remove invalid values
    df = df[(df['Quantity'] > 0) & (df['Price'] > 0)]

    # Remove duplicates
    df = df.drop_duplicates()
    print("Cleaned", df.shape[0], "records")
    return df