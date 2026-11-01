products = []

while True:
    print("\n1. Add  2. View  3. Update  4. Delete  0. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        product_id = input("Product ID: ")
        name = input("Product name: ")
        price = float(input("Price: "))
        products.append({"id": product_id, "name": name, "price": price})
        print("Product added.")

    elif choice == "2":
        for product in products:
            print(product)

    elif choice == "3":
        product_id = input("Product ID to update: ")
        product = next((p for p in products if p["id"] == product_id), None)
        if product:
            product["name"] = input("New name: ")
            product["price"] = float(input("New price: "))
            print("Product updated.")
        else:
            print("Product not found.")

    elif choice == "4":
        product_id = input("Product ID to delete: ")
        old_count = len(products)
        products = [p for p in products if p["id"] != product_id]
        print("Product deleted." if len(products) < old_count else "Product not found.")

    elif choice == "0":
        break

    else:
        print("Invalid choice.")