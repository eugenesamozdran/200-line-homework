def bubble_sort(iterable, key=None, reverse=False):

    if type(iterable).__name__ in ("str", "tuple", "set", "dict"):
        iterable = list(iterable)

    if key == None:
        pass
    else:
        iterable = list(map(key, iterable))

    for i in range(len(iterable)-1):
            if iterable[i] > iterable[i+1]:
                iterable[i], iterable[i+1] = iterable[i+1], iterable[i]
                bubble_sort(iterable)
                
    if reverse == False:
        return iterable
    else:
        return iterable[::-1]

a = {"zekrjgekrg": 3, "cgegerg": 3, "gr": 2}

a = bubble_sort(a, len, True)

print(a)
