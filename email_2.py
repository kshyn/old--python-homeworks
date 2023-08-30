#the program is the one who sent the letter more times
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname, 'r')
alibr = list()
blibr = list()
count = {}
last = list('00')
for line in fh:
    alibr = line.split()
    if 'From:' in alibr:
        blibr += ((alibr[alibr.index('From:') + 1: alibr.index('From:') + 2]))
for email in blibr:
    count[email] = count.get(email, 0) + 1
for con in count:
    if int(count.get(con)) > int(last[1]):
        last.clear()
        last.append(con)
        last.append(count.get(con))
print(*(last))
