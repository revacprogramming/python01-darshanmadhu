# Lists
ll=[]
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    for tt in line.split():
        if tt not in ll:
            ll.append(tt)

print(sorted(ll))#sort function is used to sort the list