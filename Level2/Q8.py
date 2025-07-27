string = input("Enter the string: ")
vowel="aeiou"
count=0
print(string)
for c in string:
    if c in vowel:
     count+=1
print(f"Number of vowels are {count}")      