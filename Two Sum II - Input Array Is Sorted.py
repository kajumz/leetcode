def twoSum(numbers, target):
  l=0
  r=len(numbers)-1
  sum=0
  while l<r:
    sum = numbers[l] + numbers[r]
    if sum>target:
      r-=1
    elif sum<target:
      l+=1
    else:
      return [l+1,r+1]
    
