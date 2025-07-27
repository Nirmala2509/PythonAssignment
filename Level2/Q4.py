# rotate array by D elementstowards right
arr= [1, 2, 3, 4, 5]
D=2

newlist=arr[-D:]+arr[:-D]
print(newlist)