class Solution:
    def numSteps(self, s: str) -> int:
        if s == "1":
            return 0
        
        steps = 0
        carry = 0
        
        # process from right to left (excluding MSB)
        for i in range(len(s) - 1, 0, -1):
            bit = int(s[i])
            
            if bit + carry == 1:
                # odd → add 1 + divide by 2
                steps += 2
                carry = 1
            else:
                # even → divide by 2
                steps += 1
        
        # if carry remains at MSB, one extra step
        return steps + carry