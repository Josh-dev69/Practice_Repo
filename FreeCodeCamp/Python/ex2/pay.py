# Program that compute for gross pay of workers

xh = float(input("Enter your extra hour: ")) # extra hour
xr = float(input("Enter your extra rate: ")) # extra rate

if xh > 40:
    # print("Overtime")
    reg = xh * xr # regular pay
    otp = (xh - 40.0) * (xr * 0.5) # Overtime Pay
    # print(reg, otp)
    xp = reg + otp # Total pay, extra pay included
else:
    # print("Regular")
    xp = xh * xr
print(f"Your pay is {xp}")