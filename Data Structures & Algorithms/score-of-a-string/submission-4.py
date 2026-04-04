class Solution:
    def scoreOfString(self, s: str) -> int:
        i = 0
        total = 0
        while i < len(s)-1:
            char1 = ord(s[i])
            char2 = ord(s[i+1])
            total += abs(char1-char2)
            i+=1

        return total 
        