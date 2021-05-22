def canPartition(nums):
  n=int(len(nums))
  print(n, nums)
  
  if n<=1:
    return nums
  
  total=0
  for i in range(len(nums)):
    total+=nums[i]
  
  if total %2:
    return False
  
  seen_sum = {}
  print(possiblePartition(nums, 0, total//2, 0, seen_sum))
  
def possiblePartition(nums, ctotal, target, cindex, seen_sum): 

  key=str(cindex)+"_"+str(ctotal)

  if key in seen_sum.keys():
    return seen_sum[key]
  
  
  if ctotal == target:
    return True

  if ctotal > target or cindex >= int(len(nums)):
    return False

  state = possiblePartition(nums,ctotal,target,cindex+1,seen_sum) or possiblePartition(nums, ctotal+nums[cindex], target, cindex+1,seen_sum)
  seen_sum[key]=state
  return state


from datetime import datetime

print("--->"+str(datetime.now().time()))
canPartition([1,2,1,1,1,2])
print("--->"+str(datetime.now().time()))
canPartition([1 for _ in range(200)])
print(datetime.now().time())
