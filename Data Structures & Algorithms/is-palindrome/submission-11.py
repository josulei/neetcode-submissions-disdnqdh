class Solution:
    def isPalindrome(self, s: str) -> bool:
        no_spaces = (s.replace(" ", "")).lower()
        i = 0 
        j = len(no_spaces)-1
        while(i<j):
            if no_spaces[i].isalnum() and no_spaces[j].isalnum():
                if no_spaces[i] != no_spaces[j]:
                    return False
            if not no_spaces[i].isalnum():
                i+=1
            
            if not no_spaces[j].isalnum():
                j-=1
            else:
                i+=1
                j-=1
        return True 
        