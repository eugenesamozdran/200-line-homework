def magic_range():

    for i in range(-1000, 1000):
        for x in range(-1000, 1000):
            if i is x:
                yield i

lst = []
for a in magic_range():
    lst.append(a)
        
        
print("[{0}; {1})".format(lst[0], (lst[len(lst)-1]+1)))
