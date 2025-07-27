#Create a function that takes a list and returns a new list withunique elements of the first list.
def unique(l1):
    list2=list(set(l1))
    return list2

l2=unique([1, 2, 2, 3, 4, 4, 5, 5])
print(l2)






