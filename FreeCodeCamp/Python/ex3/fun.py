def computepay(hour, rate):
    if hour > 40:
        reg = hour * rate # regular pay
        otp = (hour - 40.0) * (rate * 0.5) # Overtime Pay
        xp = reg + otp # Total pay, extra pay included
    else:
        xp = hour * rate
    print(f"Your pay is {xp}")

try:
    xh = float(input("Enter your extra hour: ")) # extra hour
    xr = float(input("Enter your extra rate: ")) # extra rate
    computepay(xh, xr)
except:
    print("Error: String Values not accepted")
    quit()
