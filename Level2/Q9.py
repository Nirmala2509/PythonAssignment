l1 = [1, 3, 4, 5, 6, 7]

for i in range(len(l1) + 2):  # intentionally go out of range
    try:
        print(f"Element at index {i}: {l1[i]}")
    except IndexError:
        print(f"IndexError: Index {i} is out of range.")
      
