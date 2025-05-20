#for week 2 of DSA
#writing all problems pertainin to this topic here
#BUY AND SELL STOCK
#L and R pointers
# BUY LOW SELLHIGH
def buy_n_sell(self,nums):
  l,r=0,1
  n=len(nums)
  mxprofit=0
  while r < n:
    if nums[l]<nums[r]:
      profit=nums[r]-nums[l]
      maxprofit=max(maxprofit,profit)
    else:
      l=r
  r+=1
  return maxprofit
