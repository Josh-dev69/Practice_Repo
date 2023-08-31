def is_year_leap(year):
    # Check if  year is leap
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): return True
    else: return False
    
def days_in_month(year, month):
    # Defining the length of the days in each month (accounting for a leap year)
    daysinmonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # check the validity of the inputs(the month and the year)
    if month >= 1 or month <= 12:
        #check if it is the 2nd month(February) and also if the year is leap
        if month == 2 and is_year_leap:
            return 29
        else:
            return daysinmonth[month]
    else:
        return None

def day_of_year(year, month, day):
    # Check if the year, month, and day are valid
    if year < 1 or month < 1 or month > 12 or day < 1 or day > days_in_month(year, month):
        return None

    # Initialize the day count to the day of the month
    day_count = day

    # Accumulate days from previous months in the year
    for m in range(1, month):
        day_count += days_in_month(year, m)

    return day_count    

#test_years = [1900, 2000, 2016, 1987]
#test_months = [2, 2, 1, 11]
#test_results = [28, 29, 31, 30]
#for i in range(len(test_years)):
#	yr = test_years[i]
#	mo = test_months[i]
#	print(yr, mo, "->", end="")
#	result = days_in_month(yr, mo)
#	if result == test_results[i]:
#		print("OK")
#	else:
#		print("Failed")

print(day_of_year(1987, 12, 31))
print(day_of_year(2023, 2, 15))  # Should return 46 (February 15th)
print(day_of_year(2024, 12, 31))  # Should return 366 (Leap year, December 31st)
print(day_of_year(2023, 4, 31))  # Invalid day for April, should return None
print(day_of_year(2023, 13, 1))