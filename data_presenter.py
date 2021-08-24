open_file = open("CupcakeInvoices.csv")

for line in open_file:
    print(line)


for line in open_file:
    row = line.split(",")
    print(row[2])


for line in open_file:
    x = line.split(",")
    print(x[4])


for line in open_file:
    y = line.split(",")
    total = float(y[3]) * float(y[4])
    print(total)


total = 0
for line in open_file:
    y = line.split(",")
    total += int(y[3]) * float(y[4])
    # total = total + int(y[3]) * float(y[4]) -> the other way to write the formula above
print(total)


open_file.close()