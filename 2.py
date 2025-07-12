# How many rows you want
rows=int(input("Enter the number of rows: "))

# Starting number
num = 1

# Loop through rows
for i in range(1, rows + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()  # Go to the next line