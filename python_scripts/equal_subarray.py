def canPartition(nums):
  n=int(len(nums))
  
  if n<=1:
    return nums
  
  total=0
  for i in range(len(nums)):
    total+=nums[i]
  
  if total %2:
    return False
  
  print(possiblePartition(nums, 0, sum//2, 0))
  
def possiblePartition(nums, ctotal, target, cindex): 
  if ctotal == target:
    return True

  if ctotal > target or cindex >= int(len(nums)):
    return False

  return possiblePartition(nums,ctotal,target,cindex+1) or possiblePartition(nums, ctotal+nums[cindex], target, cindex+1)
