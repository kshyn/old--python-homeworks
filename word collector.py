#the program compiles a dictionary of words used in the text
fname = input("Enter file name: ")
fh = open(fname, 'r')
#first, information is collected about all the words in the text in general and sent to the list
alibr = list()
blibr = list()
for line in fh:
    alibr = alibr + line.split()
#unique words are determined and grouped into a separate list
for word in alibr:
    if word not in blibr:
        blibr.append(word)
#sorting
blibr.sort()
print(blibr)
