def battleship(bs):
  if int(len(bs)) <=0:
    return 0
  
  ships=0
  for row in range(len(bs)):
    for col in range(len(bs[row])):
      if bs[row][col] == ".":
        continue
      
      if bs[row-1][col] == "X" and row>0:
        continue
      
      if bs[row][col-1] == "X" and col>0:
        continue
      
      ships+=1
      
  return ships
                     
