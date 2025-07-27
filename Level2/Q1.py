#Write a Python program to find the common elements betweentwo lists.

l1=[1, 2, 3, 4, 5] 
l2 = [4, 5, 6, 7, 8]
l3=[]
n=0
m=0
for i in l1:
    if i in l2:
        l3.append(i) 
print(l3)  


