#LCM of a number

def compute_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def compute_lcm(a, b):
    gcd = compute_gcd(a, b)
    lcm = (a * b) // gcd
    return lcm

# Input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate LCM
lcm = compute_lcm(num1, num2)

# Output
print(f"The LCM of {num1} and {num2} is: {lcm}")

