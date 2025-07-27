#to check if a string is an anagram ofanother string.

str1=input("Enter the first string: ")
str2=input("Enter the second string: ")

sort_str1=''.join(sorted(str1))
sort_str2=''.join(sorted(str2))
print(str1)
print(str2)

if sort_str1==sort_str2:
    print(f"{str1} is anagram of {str2} ")
else:
     print(f"{str1} is not an anagram of {str2} ")    
