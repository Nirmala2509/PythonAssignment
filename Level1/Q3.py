#Calculate thepercentage and grade

Phy=int(input("Enter the number for physics: "))
Chem=int(input("Enter the number for chemistry: "))
Bio=int(input("Enter the number for biology: "))
Math=int(input("Enter the number for Math: "))
Comp=int(input("Enter the number for Computer: "))

per=(Phy+Chem+Bio+Math+Comp)/500*100
print(f"{per}%")

if per>=90:
    print("Grade A")
elif per>=80:
    print("Grade B")
elif per >=70:
    print("Grade C")
elif per >=60:
    print("Grade D")
elif per >=40:
    print("Grade E")    
else:
    print("Grade F")                
