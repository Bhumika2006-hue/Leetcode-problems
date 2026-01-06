class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total_sum = 0
        min_abs_val = float('inf')
        negative_count = 0
        
        for row in matrix:
            for val in row:
                # Add the absolute value to the total sum
                abs_val = abs(val)
                total_sum += abs_val
                
                # Keep track of the smallest absolute value in the matrix
                if abs_val < min_abs_val:
                    min_abs_val = abs_val
                
                # Count how many negative numbers we have
                if val < 0:
                    negative_count += 1
        
        # If the number of negatives is even, we can make all elements positive
        if negative_count % 2 == 0:
            return total_sum
        else:
            # If odd, one element must remain negative. 
            # We subtract twice the smallest value (once to remove it from 
            # the positive sum, and once to account for its negative value).
            return total_sum - (2 * min_abs_val)
        