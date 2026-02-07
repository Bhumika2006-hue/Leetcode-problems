class Solution:
    def minimumDeletions(self, s: str) -> int:
        deletions = 0
        count_b = 0
        
        for ch in s:
            if ch == 'b':
                count_b += 1
            else:  # ch == 'a'
                deletions = min(deletions + 1, count_b)
        
        return deletions
