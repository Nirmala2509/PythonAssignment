#Factorial of a num

def factorial(num):
 fact=1
 for i in range(1,num+1):
   
    fact=i*fact
    #print(fact)
 print(f"factorial of number {num} is {fact}")    

p=factorial(10)