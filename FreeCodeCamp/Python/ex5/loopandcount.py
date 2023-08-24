# Encapsulate this function named count, and
# generalize it so that it accepts the string and the letter as arguments.

def count(word, letter):
    count = 0
    for char in word:
        if char == letter:
            count += 1
    return count




word = input("Enter the word to loop through: ")
char = input("Enter the character to count: ")

print(count(word, char))