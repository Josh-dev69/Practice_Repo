import random
number = random.randint(-10000, 10000)
last_dig = abs(number) % 10
if last_dig > 5:
    print(f"The Last digit of {number:d} is {last_dig:d} and is greater than 5")
elif last_dig == 0:
    print(f"The Last digit of {number:d} is {last_dig:d} and is 0")
elif last_dig < 6 and last_dig != 0:
    print(f"The Last digit of {number:d} is {last_dig:d} and is less than 6 and not 0") 