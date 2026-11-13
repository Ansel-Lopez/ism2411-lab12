
# --- Reflection Questions ---
# 1. Python makes it easier to automate repetitive tasks like reading
#    and cleaning large CSV files. Excel is easier for quickly viewing
#    data, making changes manually, and creating charts.
# 2. A business could use an append mode log to track daily sales.
#    Append mode is useful because it adds new records without
#    deleting the previous sales information.


import csv

from datetime import datetime

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    header = next(reader)
    print("Header:", header)

    for row in reader:
        print(row)

total_revenue = 0

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])

        total = price * quantity
        total_revenue += total

        print(f"{product}: {quantity} units x ${price:.2f} = ${total:.2f}")

print(f"Overall Revenue: ${total_revenue:.2f}")

original_count = 0
cleaned_count = 0

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    with open("data/cleaned.csv", "w", newline="") as output:
        writer = csv.writer(output)
        writer.writerow(["Product", "Price", "Qty", "Total"])

        for row in reader:
            original_count += 1
            product = row[0]
            price = float(row[1])
            quantity = int(row[2])
            total = price * quantity

            if total > 100:
                writer.writerow([product, price, quantity, total])
                cleaned_count += 1

print("Original rows:", original_count)
print("Cleaned rows:", cleaned_count)

total_revenue = 0

with open("data/sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity
        total_revenue += total

        print(f"{product}: ${total:.2f}")

print(f"Total Revenue: ${total_revenue:.2f}")

product_totals = {}

with open("data/sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])
        total = price * quantity

        if product in product_totals:
            product_totals[product] += total
        else:
            product_totals[product] = total

for product in product_totals:
    print(f"{product}: ${product_totals[product]:.2f}")


# Exercise 8: Append mode log
now = datetime.now()

with open("data/run_log.txt", "a") as file:
    file.write(f"{now}: Total Revenue = ${total_revenue:.2f}\n")

print("Run log updated.")

