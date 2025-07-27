#find the number ofpairs of elements in the array whose sum is equal to K

arr=[1, 2, 3, 4, 5]
k=6
counter=0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==k:
         counter+=1
print(f"Pair count {counter}")

    

