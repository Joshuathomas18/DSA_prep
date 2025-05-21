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


#Max longest substring
def longest_substring(self,s):
  charset=set()
  l=0
  res=0
  for r in range(len(nums)):
    while s[r] in charset:
      charset.remove(s[l])
      l+=1
    charset.add(s[r])
    res=max(res,r-l+1)
  return res
