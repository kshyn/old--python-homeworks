#the program compiles a list of e-mails that sent letters
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname, 'r')
alibr = list()
count = 0
for line in fh:
    alibr = line.split()
    if 'From:' in alibr:
        print(*(alibr[alibr.index('From:') + 1: alibr.index('From:') + 2]))
        count += 1
print("There were", count, "lines in the file with From as the first word")
