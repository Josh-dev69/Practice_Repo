my_list = [3, 41, 12, 9, 74, 15]
smallest = my_list[0]
print("Before:", smallest)
for itervar in my_list:
    if itervar < smallest:
        smallest = itervar
        break
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)