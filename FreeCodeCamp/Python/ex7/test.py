# word = 'brontosaurus'
#d = dict()
#for c in word:
#    if c not in d:
#        d[c] = 1
#    else:
#        d[c] = d[c] + 1
#print(d)

#e = dict()
#for c in word:
#    e[c] = e.get(c,0) + 1
#print(e)

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print(counts)