import csv
with open('data.csv','r') as csvfile:
 data = csv.DictReader(csvfile)
 print("CGPA of SEM 1 & 2")
 print("---------------------------------")
 for row in data:
   print(row['SEM 1 SGPA'] ,row['SEM 2 SGPA'])
