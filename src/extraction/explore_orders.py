from src.extraction.read_csv import read_csv_file

def main():
    file_path = "data/raw/olist_orders_dataset.csv"

    df = read_csv_file(file_path)

    print("\n--- FIRST 5 ROWS ---")
    print(df.head())

    print("\n--- DATASET DIMENSIONS ---")
    print(df.shape)

    print("\n--- DATA TYPES ---")
    print(df.dtypes)

    print("\n--- NULL VALUES ---")
    print(df.isnull().sum())

    print("\n--- DUPLICATED ROWS ---")
    print(df.duplicated().sum())

    print("\n--- HOW MANY ORDERS IN EACH STATUS ---")
    print(df["order_status"].value_counts())

    print("\n--- UNIQUED IDENTIFIERS FOR ORDERS ---")
    print(df["order_id"].nunique())

    print("\n--- UNIQUED IDENTIFIERS FOR CUSTOMERS ---")
    print(df["customer_id"].nunique())

    print("\n--- PORCENTAJE OF NULL VALUES FOR COLUMN ---")
    print(df.isnull().mean() * 100)

if __name__ == "__main__":
    main()
