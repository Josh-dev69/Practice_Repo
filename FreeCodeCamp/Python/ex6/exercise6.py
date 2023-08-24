# A program that prompts for a file name, then opens that file and reads
# through the file, looking for lines of the form

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    print(line)
print("Done")