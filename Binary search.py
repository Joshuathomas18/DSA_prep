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

#2D binary search

#FIRST FIND ROW
#THEN BINARY SEARCH IN COL

def find_numer(self,matrix,target):
 
 
#KOKO BANANAS
#use hours binary search(max(list) and 1)
#apply if-else

def find_hours(self,nums,h):
 
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res
#min value in sorted rotated array

#find left sorted or right sorted region
#apply B.S there
def min_value(self,nums):
 n=len(nums)
 l,r=0,n-1
 res=nums[0]
 while l<=r:
  if nums[l]<=nums[r]:
   res=min(res,nums[l])
  m=(l+r)//2
  if nums[m]>=nums[l]:
   l=m+1
   res = min(res,nums[m])
  else:
   r=m-1
   res = min(res,nums[m])
 return res

