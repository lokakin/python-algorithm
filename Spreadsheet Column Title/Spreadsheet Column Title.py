class Solution:
  def convertToTitle(self, n):
    result = ''
    distance = ord('A')
    while n > 0:
      
      y = (n-1) % 26
      
      n = (n-1) // 26
     
      s = chr(y+distance)
      result = ''.join((s, result))
    return result

input1 = 1
input2 = 456976
input3 = 28
print(Solution().convertToTitle(input1))

print(Solution().convertToTitle(input2))
print(Solution().convertToTitle(input3))