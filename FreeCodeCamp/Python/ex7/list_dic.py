# Initialize an empty dictionary
word_dictionary = {}

# Open the file for reading
with open("words.txt", "r") as file:
    # Read each line (assuming each word is on a separate line)
    for line in file:
        # Remove leading and trailing whitespaces, if any
        word = line.strip()        
        # Store the word in the dictionary with a placeholder value (e.g., True)
        word_dictionary[word] = True

# Prompt the user to input a word to check
word_to_check = input("Enter a word to check: ")

# Check if the word is in the dictionary
if word_to_check in word_dictionary:
    print(f"{word_to_check} is in the dictionary.")
else:
    print(f"{word_to_check} is not in the dictionary.")



