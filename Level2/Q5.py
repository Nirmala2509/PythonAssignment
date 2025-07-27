# determines the average temperature, highesttemperature, and lowest temperature

def calc_temperature(l1):
    avg_temp=sum(l1)/len(l1)
    high_temp=max(l1)
    low_temp=min(l1)
    print(f'Average Temperature : {avg_temp}')
    print(f'Highest Temperature : {high_temp}')
    print(f'Lowest Temperature :  {low_temp}')

l2=calc_temperature([25, 28, 21, 24, 27])    

