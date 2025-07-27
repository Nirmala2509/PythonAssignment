# finds the median of a list of numbers.

l1 = [7, 2, 5, 1, 9, 3]
l2 = list(set(l1))
print(l2)
x = len(l2)
#print(x)
if len(l2) % 2 == 0:

    median = (l2[x//2]+l2[(x//2)-1])//2
    print(f"median is even {median}")
else:
    median = l2[x// 2]
    print(f"median is odd {median}") 