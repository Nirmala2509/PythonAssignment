#Python program to calculate the sum of digits of a givennumber until the sum becomes a single-digit number

def sum_until_single_digit(n):
    while n >= 10:
        total = 0
        while n > 0:
            total += n % 10
            n //= 10
        n = total
    return n

# Input
num = int(input("Enter a number: "))

# Final Output
print(sum_until_single_digit(num))


