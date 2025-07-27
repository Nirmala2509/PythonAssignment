#Sum of all odd numbers

def sum_odd(a,b):
    sum=0
    for i in range(a,b):
        if i %2!=0:
            sum=sum+i
    print(f"Sum of odd numbers : {sum}")

p=sum_odd(1,10)            
