import csv

# Exercise 2: Read and print raw rows
with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)