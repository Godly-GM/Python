import csv
with open('data.csv','r') as csvfile:
 data = csv.DictReader(csvfile)
 print("Name and Roll No")
 print("---------------------------------")
 for row in data:
   print(row['Name'] ,row['Roll No'])