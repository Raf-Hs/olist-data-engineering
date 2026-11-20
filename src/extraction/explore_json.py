from src.extraction.read_json import read_json_file

def main():
    file_path = "data/samples/sample_order.json"

    # 1. Read JSON
    data = read_json_file(file_path)

    # 2. Inspect the main structure
    print("\n--- DATA TYPE ---")
    print(type(data))

    # 3. Access order information
    print("\n--- ORDER INFORMATION ---")
    print(f"Order ID: {data.get('order_id')}")
    print(f"Customer ID: {data.get('customer_id')}")
    print(f"Order Status: {data.get('order_status')}")
    print(f"Price: {data.get('price')}")
    print(f"Approved: {data.get('approved')}")
    print(f"Delivery: {data.get('delivery')}")

    # 4. Access nested items
    print("\n--- ORDER ITEMS ---")

    items = data.get("items", [])

    for item in items:
        print(f"Product ID: {item.get('product_id')}")
        print(f"Quantity: {item.get('quantity')}")

    # 5. Calculate total quantity
    total_quantity = sum(
        item.get("quantity", 0) for item in items
    )

    print("\n--- SUMMARY ---")
    print(f"Total products: {len(items)}")
    print(f"Total quantity: {total_quantity}")


if __name__ == "__main__":
    main()