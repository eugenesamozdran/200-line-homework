def magic_range():

    for i in range(-1000, 1001):
        yield i

lst = []
for a in magic_range():
    for i in magic_range():
        if a is i:
            lst.append(a)
        
        
print("[{0}; {1})".format(lst[0], (lst[len(lst)-1]+1)))
