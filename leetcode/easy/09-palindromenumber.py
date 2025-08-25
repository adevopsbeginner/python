class Solution:
  def isPalindrome(self, x: int) -> bool:
    strx = str(x)
    print(strx)
    ll = len(strx)
    for ii in range (ll//2+1):
      if strx[ii] == strx[ll-1-ii]:
        continue
      else:
        return False

    return True

if __name__ == "__main__":
  app = Solution()
  print(app.isPalindrome(-12321))
