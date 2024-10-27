import csv

with open("Cleaned_dataset.csv", 'r') as file:
    csvreader = csv.reader(file)

    for row in csvreader:
        print(row)