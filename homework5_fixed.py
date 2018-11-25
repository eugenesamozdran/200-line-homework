import string

def is_palindrome(a):

    # making 2 copies of the string
    # first one is in lowercase and without spaces
    # second one is the reverted version of the first
    
    a1 = a.replace(" ","").lower()
    b = a1[::-1]

    if a1 == b:
        print("YES")
    else:
        print("NO")

# allowed symbols is required for checking if any of argument characters do not match the required pattern
ALLOWED_SYMBOLS = string.ascii_lowercase + " " + string.ascii_uppercase + string.digits

a = "7PalinDr ome EmordNi lap7"

# checking if the string has at least 1 alphanumeric character or space
# and if it matches the required pattern

while len(a) == 0:
        a = input("Please enter a string containing at least one alphanumeric character and/or space: ")
        break

for char in a:
    while char not in ALLOWED_SYMBOLS:
        a = input("Please enter a string containing only alphanumeric characters and spaces (if necessary): ")
        break

is_palindrome(a)
