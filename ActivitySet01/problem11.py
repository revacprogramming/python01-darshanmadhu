name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
time={}
final=[]
for line in handle:
  if line.startswitth("from:"):continue
  if line.startswitth("from:"):continue
  index=line.find(":")
  store=line[index-2:index]
  if store in time:
    time[store]+=1
  else:
    time[store]=1

final=list(time.items())
final.sort()
for a,b in final:
  print(a,b)