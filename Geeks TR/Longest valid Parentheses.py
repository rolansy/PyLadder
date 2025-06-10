

class Solution:
    def maxLength(self, s):
        stack = [-1]  # Initialize with -1 as a base for calculating lengths
        max_length = 0
                
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)  # Push index of opening bracket
            else:  # s[i] == ')'
                stack.pop()  # Pop the last opening bracket index
                if not stack:  # If stack is empty, push current index as new base
                    stack.append(i)
                else:
                    # Calculate length from current position to the last unmatched position
                    max_length = max(max_length, i - stack[-1])
                    
        return max_length
