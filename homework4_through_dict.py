def find_most_frequent(text):

    # making a new string in lowercase
    # and replacing punctuation marks in it with spaces
    sub_str = text.lower()
    translation_table = dict.fromkeys(map(ord, ",.:;!?-"), " ")
    sub_str2 = sub_str.translate(translation_table)
    
    # creating a list of separate words and getting rid of spaces
    lst = [x for x in sub_str2.split(" ") if x!=""]

    # forming a dictionary with a word from 'lst' as a key
    # and the number of these words in 'lst' as a value
    count_dict = {z: lst.count(z) for z in lst}
            
    final_lst = []
    for i in count_dict:
        if count_dict[i] == max(count_dict.values()):
            final_lst.append(i)
        
    # printing the list (if there is more than one word, the list is sorted)
    if len(final_lst) == 1:
        print(final_lst)
    else:
        final_lst.sort()
        print(final_lst)

find_most_frequent("Tom? WHO ARE YOU, TOm?! You are fool, I:am:Lord-wOldemOrt")
