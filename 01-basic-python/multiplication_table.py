# Multiplication table

# Ask the user for a number and print the times table from 1 to 12
num = int(input("Enter a number: "))

for i in range(1, 13):
    print(f"{i} x {num} = {i * num}")
