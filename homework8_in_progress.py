from collections.abc import Iterable

def bubble_sort(iter_obj, key=None, reverse=False):
    
    # first, we check if argument is iterable
    # if yes and if it is not 'list', we convert the argument to a list
    
    if isinstance(iter_obj, Iterable):

        # here we check if some function was passed as a key
        # and modify our iterable applying the function to all its elements
        
        if key == None:
            iter_obj = list(iter_obj)
            pass
        else:
            iter_obj = list(map(key, iter_obj))

        # this is the sorting loop itself
        for i in range(len(iter_obj)):
            for y in range(len(iter_obj)-i-1):
                if iter_obj[y] > iter_obj[y+1]:
                    iter_obj[y], iter_obj[y+1] = iter_obj[y+1], iter_obj[y]
                    
        # here we check if the result should be reversed or not            
        if reverse:
            return iter_obj[::-1]
        return iter_obj

    else:
        raise TypeError

a = [{"value": 42}, {"value": 32}, {"value": 40}, {"value": 56}, {"value": 11}]

a = bubble_sort(a, lambda x: x["value"])

print(a)
