# Write a Python program to check if a number is a power of two using recursion.
 
def recnum(num):
    if num==1 :  
     print(f"Number  {num} is power of 2") 
    elif num %2!=0 or num==0:
     
     print(f"Number  {num} is not power of 2") 
    else:
      recnum(num//2)

   
num=int(input("Enter the number:"))
recnum(num)              
            





    
    
    