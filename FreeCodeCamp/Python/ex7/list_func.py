# A function called 'chop' that takes a list and modifies it,
# removing the first and last elements, and returns None.
# Then write a function called middle that takes a list and 
# returns a new list that contains all but the first and last elements.

def chop(mylist):
    del mylist[0]
    del mylist[-1]

def middle(my_list):
    return my_list[1:-1]


new_list = [1, 4, 5, 7, 8, 9]

print(chop(new_list))
print(middle(new_list))