def calculate_percentage(x, y):
    percentage = (x / y) * 100
    return round(percentage)

def main():
    while True:
        try:
            fraction = input("Fraction: ")
            x, y = map(int, fraction.split('/'))
            if x <= 0 or y <= 0 or x > y:
                continue
            percentage = calculate_percentage(x, y)

            if percentage <= 0:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer fraction in the format X/Y.")
        except ZeroDivisionError:
            print("Invalid input. Y cannot be zero.")
        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
main()
