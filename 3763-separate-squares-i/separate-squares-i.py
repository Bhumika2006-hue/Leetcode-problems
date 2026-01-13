class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area = 0
        min_y = float('inf')
        max_y = float('-inf')
        
        for x, y, l in squares:
            total_area += l * l
            min_y = min(min_y, y)
            max_y = max(max_y, y + l)
            
        target_area = total_area / 2
        
        # Binary search for the y-coordinate
        low = min_y
        high = max_y
        
        # 100 iterations provide precision far beyond 10^-5
        for _ in range(100):
            mid = (low + high) / 2
            area_below = 0
            
            for x, y, l in squares:
                if mid <= y:
                    # Square is entirely above the line
                    continue
                elif mid >= y + l:
                    # Square is entirely below the line
                    area_below += l * l
                else:
                    # Line intersects the square
                    # Height below the line is (mid - y)
                    area_below += l * (mid - y)
            
            if area_below < target_area:
                low = mid
            else:
                high = mid
                
        return low