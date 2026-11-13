import csv

# Exercise 3: Skip the header
with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    header = next(reader)
    print("Header:", header)

    for row in reader:
        print(row)