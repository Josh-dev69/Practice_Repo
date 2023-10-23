def has_minimum_length(s):
    return len(s) >= 2

def has_maximum_length(s):
    return len(s) <= 6

def no_numbers_in_middle(s):
    return s[2:-1].isdigit()

def first_number_not_zero(s):
    return s[-1] != '0'

def no_punctuation(s):
    return all(c.isalnum() for c in s)

def is_valid(s):
    if has_minimum_length(s) and has_maximum_length(s) and no_numbers_in_middle(s) and first_number_not_zero(s) and no_punctuation(s):
        return True
    else:
        return False

def main():
    user_input = input("Enter a vanity plate: ").strip()

    if is_valid(user_input):
        print("Valid")
    else:
        print("Invalid")

main()
