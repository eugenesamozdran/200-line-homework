import string

def count_holes(n):

    HOLE_DICT = {
                    "0": 1,
                    "1": 0,
                    "2": 0,
                    "3": 0,
                    "4": 1,
                    "5": 0,
                    "6": 1,
                    "7": 0,
                    "8": 2,
                    "9": 1,
                    "-": 0
                }

    hole_number = 0
    ALLOWED_SYMBOLS = tuple("-" + string.digits)
    
    for char in str(n):
        if char not in ALLOWED_SYMBOLS:
            print("ERROR")
            break
    else:
        for char in str(int(n)):
            hole_number += HOLE_DICT[char]
        print("The number of holes is {}".format(hole_number))
       
count_holes("-168")
