#find the number of customers that walked away without using a computer.

def customers_who_left(N, S):
    using_computers = set()
    seen_customers = set()
    walk_away = 0
    occupied = 0

    for c in S:
        if c not in seen_customers:
            # First time seeing the customer (arrival)
            seen_customers.add(c)
            if occupied < N:
                using_computers.add(c)
                occupied += 1
            else:
                walk_away += 1
        else:
            # Second time seeing the customer (departure)
            if c in using_computers:
                using_computers.remove(c)
                occupied -= 1

    return walk_away

print(customers_who_left(3, 'GACCBDDBAGEE'))

print(customers_who_left(1, 'ABCBAC'))
        