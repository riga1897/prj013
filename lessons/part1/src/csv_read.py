import csv

# with open('../data/file.csv') as file:
#     reader = csv.reader(file)
#     next(reader)
#     for row in reader:
#         if float(row[1]) > 29:
#             print(row)

with open('../data/file.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if float(row['Age']) > 29:
            print(row)