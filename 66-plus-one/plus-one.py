class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        # Traverse the array from right to left
        for i in range(n - 1, -1, -1):
            # If the current digit is less than 9, increment it and we are done
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            # If the digit is 9, it becomes 0 (and the loop continues to handle the carry)
            digits[i] = 0
            
        # If the loop completes, it means all digits were 9 (e.g., [9, 9, 9])
        # We need an extra 1 at the front (e.g., [1, 0, 0, 0])
        return [1] + digits
        