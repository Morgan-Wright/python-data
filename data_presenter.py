open_file = open("CupcakeInvoices.csv")

# for row_data in open_file:
    # print(row_data)

for row in open_file:
    values = row.split(",")
    print(row[2])

for row in data:
    values = row.split(",")
    total = int(values[3]) * float(values[4])
    print(total)

total = 0
for row in data:
  values = row.split(',')
  total = total + (int(values[3]) * float(values[4]))
print(total)

open_file.close()
