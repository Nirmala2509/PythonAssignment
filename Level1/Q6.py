#Python program to check if a given number is a perfectnumber
num=int(input("Enter the number: "))
sum=0
for i in range(1,num): 
    if num%i==0:       
        sum=sum+i
#Checking if perfect no or not.        
if sum==num:
          print(f"{num} is a perfect number.")
else:
          print(f"{num} is not a perfect number.")        
       
