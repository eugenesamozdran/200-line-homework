import string

def count_holes(n):

    # defining the number of 'holes' for each digit string representation
    HOLE_DICT = {
                    "0": 1,
                    "4": 1,
                    "6": 1,
                    "8": 2,
                    "9": 1,
                }

    # allowed symbols is required for checking if any of argument characters do not match integer number pattern
    ALLOWED_SYMBOLS = "-" + string.digits
    hole_number = 0
    
    # printing error message if the argument does not look like the number at all (or contains characters different from digits or '-')
    # and counting number of 'holes'
    for char in str(n):
        if char not in ALLOWED_SYMBOLS:
            print("ERROR")
            break
    else:
        # the argument is converted to integer and back to string in order to get rid of unnecessary zeroes at the beginning (if any)
        for char in str(int(n)): 
            hole_number += HOLE_DICT.get(char, 0)
        print("The number of holes is {}".format(hole_number))
       
count_holes(-987345)
