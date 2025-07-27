#Write a Python program to find the number of stones in each pile.

# Input: Total number of stones
n = int(input("Enter the number of stones: "))

# Determine the starting number based on whether n is even or odd
if n % 2 == 0:
    start = 2  # Even starting value
else:
    start = 1  # Odd starting value

piles = []     # To store number of stones in each pile
current = start
total = 0

# Build strictly increasing sequence of same-parity numbers
while total + current <= n:
    piles.append(current)
    total += current
    current += 2  # Next even or odd number

# Adjust the last pile to make exact total
if total < n:
    piles[-1] += (n - total)

# Output the result
print("Stones in each pile =", piles)
