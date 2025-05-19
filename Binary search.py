#FOR WEEK 2 OF DSA 
#SOLVE ALL QUESTIONS UNDER THIS TOPIC HERE
#find number desired
#Approach
 # 1. use mid
 # 2. move left or right acc to the target

def find_target(self,nums,target):
  n=len(nums)
  l,r=0,n-1
  while l<=r:
    mid=l+(r-l)//2
    if nums[mid]>target:
      r=mid-1
    elif nums[mid]<target:
      l=mid+1
    else:
      return mid
  return -1


    
