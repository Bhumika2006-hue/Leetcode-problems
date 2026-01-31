class Solution:
    def nextGreatestLetter(self, letters, target):
        left, right = 0, len(letters) - 1
        ans = letters[0]   # default for wrap-around
        
        while left <= right:
            mid = (left + right) // 2
            if letters[mid] > target:
                ans = letters[mid]
                right = mid - 1
            else:
                left = mid + 1
        
        return ans
