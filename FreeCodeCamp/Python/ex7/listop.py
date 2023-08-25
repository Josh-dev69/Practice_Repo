# Program that reads user's input until the user enters "done"
# Once done prints the sum, total counts and average of the user's input
def loop_function():
    my_list = []
    while True:
        try:
            u_in = input("Enter a number: ")
            if u_in == "done":
                break
            a = int(u_in)
            my_list.append(a)
        except:
            print("Invalid input")
    
    total = sum(my_list)
    list_len = len(my_list)
    average = total / list_len
    print("ALL DONE")
    print(total, list_len, average)


loop_function()