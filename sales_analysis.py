
import csv

total_revenue = 0
transactions = 0

with open("sales.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        quantity = int(row["quantity"])
        price = float(row["price"])

        revenue = quantity * price
        total_revenue += revenue
        transactions += 1

print("Sales Analysis Report")
print("---------------------")
print(f"Transactions: {transactions}")
print(f"Total revenue: ${total_revenue:.2f}")

if transactions > 0:
    average = total_revenue / transactions
    print(f"Average revenue: ${average:.2f}")
