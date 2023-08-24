# Program that reads user's input until the user enters "done"
# Once done prints the sum, total counts and average of the user's input
def loop_function():
    count = 0
    total = 0
    while True:
        try:
            u_in = input("Enter a number: ")
            if u_in == "done":
                break
            a = int(u_in)
            total += a
            count += 1
            average = total / count
        except:
            print("Invalid input")
    
    print("ALL DONE")
    print(total, count, average)


loop_function()