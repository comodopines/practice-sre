import os, sys

d1='dataset2.csv'
d2='dataset1.csv'

if not os.path.exists(d1) or not os.path.exists(d2):
  sys.exit()
delim=','
bip_dinos = {}
with open(d1, "r") as d1csv:
  for line in d1csv:
   dino = line.strip().split(delim) 
   name=dino[0]
   sl=dino[1]
   bp=dino[2]
   
   if bp.lower() == "bipedal":
     try:
       bip_dinos[name]=[float(sl)] 
     except ValueError:
       continue
print(bip_dinos)
#fin_dinos={}
g=9.8
with open(d2, "r") as d2csv:
  for line in d2csv:
    dino = line.strip().split(delim)
    name=dino[0]
    ll=dino[1]
    try:
      sl=float(bip_dinos[name][0])
      ll=float(ll)
      speed = ((ll /sl) -1) * (ll *g)**0.5
      #fin_dinos[name]=float(speed)
      bip_dinos[name].append(ll)
      bip_dinos[name].append(speed)
    except ValueError:
      pass
    except KeyError:
      pass
#print(fin_dinos)

print(bip_dinos)
for k in list(bip_dinos.keys()):
  if len(bip_dinos[k]) <3:
    #bip_dinos.pop(k)
    bip_dinos[k].append(float('-inf'))
    bip_dinos[k].append(float('-inf'))
print(bip_dinos)
for name,speed in sorted(bip_dinos.items(), key=lambda x:x[1][2], reverse=True):
  print(name)
