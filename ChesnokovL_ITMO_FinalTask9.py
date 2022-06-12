import random

mass = random.sample([i for i in range(10)], 10)
key = mass[6]

def Search_In_Non_Sorted_Massive(mass,key):
    for i in range(len(mass)):
        if mass[i] == key:
            return True
    return False

print(Search_In_Non_Sorted_Massive(mass,key))
print(mass)