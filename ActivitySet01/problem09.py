# Lists
#problem09

filename = "dataset/mbox-short.txt"

fh = open(filename)
ans = 0
count = 0
#lists
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    pod = line
    pod = pod.find(':')
    pod = line[pod+1:]
    pod = pod.strip()
    pod = float(pod)
    ans = ans + pod
    count += 1
average = ans/count
print("Average spam confidence:", average)