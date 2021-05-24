import os, sys, time
import collections

if len(sys.argv) < 3:
  print("Usage:")
  sys.exit(0)

file=sys.argv[1]

if not os.path.exists(file):
  print("File missing")
  sys.exit(0)

try:
  n_line=int(sys.argv[2])
except ValueError:
  sys.exit()

if n_line <=0:
  print("usage:", n_line)
  sys.exit(0)

lines = collections.deque()
with open(file, "r") as f1:
  f1.seek(0,os.SEEK_END)
  limit=f1.tell()
  f1.seek(0,os.SEEK_SET)
  curr=0
  
  lines_seen=0

  while curr < limit:
    #if int(len(lines)) >= n_line:
    if int(lines_seen) >= n_line:
      #lines.pop(0)
      lines.popleft()
      lines_seen-=1
    
    lines.append(f1.readline().rstrip())
    lines_seen+=1
    
    f1.seek(0,os.SEEK_CUR)
    curr=f1.tell()
    

  for line in lines:
    print(line)
  
  while True:
    line=f1.readline().rstrip()
    if not line:
      #print("sleeping as no new line")
      time.sleep(5)
    else:
      print(line)
