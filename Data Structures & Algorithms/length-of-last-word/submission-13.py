class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        i = len(s) -1
        firstLetter = False
        if i!=0: 
            while i>=0:
                if not firstLetter and s[i] != " ":
                    firstLetter = True 
                    length+=1
                elif s[i] != " " and firstLetter:
                    length+=1
                elif firstLetter and s[i] == " ":
                    break
                i-=1
        else: 
            if len(s) == 1:
                length = 1
        return length