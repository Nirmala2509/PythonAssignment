
string_input=input("Enter the string: ")
m=0
n=0
for c in string_input:
    if c.isalpha():
        m+=1

    elif c.isdigit():
        n+=1
print(f"Alphabets: {m}")
print(f"Numbers: {n}")