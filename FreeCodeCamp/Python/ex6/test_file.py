# This program counts and prints the total lines in a file
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)


# A program to read through a file and print the contents of
# the file (line by line) all in upper case.
fh = open('mbox-short.txt')
for line in fh:
    ne = line.rstrip()
    print(ne.upper())