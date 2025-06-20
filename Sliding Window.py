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
res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[::])
                return

            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)

        backtrack(0, [])
        return res

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS,COLS=len(board),len(board[0])
        path=set()

        def dfs(r,c,i):
            if i ==len(word):
                return True
            if (r < 0 or c < 0 or r >=ROWS or c >= COLS
            or word[i] != board[r][c] or (r,c) in path ):
                return False
            path.add((r,c))
            res=(dfs(r+1,c,i+1)
            or dfs(r-1,c,i+1) 
            or dfs(r,c+1,i+1)
            or dfs(r,c-1,i+1))
            path.remove((r,c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True

        return False
