from itertools import dropwhile

lst = list(range(0, 10))

a = list(map(lambda x: x**2, lst))
print("map func for 'lst':", a)

b = list(filter(lambda x: x%2, lst))
print("filter func for 'lst':", b)

d = list(dropwhile(lambda x: x<4, lst))
print("printing 'lst' elements starting from the first one that don't meet the condition:", d)

y = 4
z = 4
c = [(y is z), (z is y), (y != 4), (z == 4)]
print("are all the elements of 'c' true? -", all(c))

print("are any of the elements of 'c' true? -", any(c))
