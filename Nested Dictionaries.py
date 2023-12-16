allGuests = {"Alice": {"apples": 5, "pretzels": 12},
             "Bob": {"ham sandwiches": 3, "apples": 2},
             "Carol": {"cups": 3, "apple pies": 1}}

def totalBrought(guests,item):
    numBrought = 0
    for k, v in guests.items():
        numBrought += v.get(item,0)
    return numBrought

print("Number of things being brought: ")
print(f" - Apples         {totalBrought(allGuests,'apples')}")
print(f" - Cups           {totalBrought(allGuests,'cups')}")
print(f" - Cakes          {totalBrought(allGuests,'cakes')}")
print(f" - Ham sandwiches {totalBrought(allGuests,'ham sandwiches')}")
print(f" - Apple Pies     {totalBrought(allGuests,'apple pies')}")


