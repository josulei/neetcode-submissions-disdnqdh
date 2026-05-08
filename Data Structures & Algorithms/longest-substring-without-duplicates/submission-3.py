class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_set = set()
        left = 0
        maximumLen = 0
        for right in range(len(s)):
            if s[right] in my_set:
                maximumLen = max(maximumLen, len(my_set))
                while s[left] != s[right]:
                    my_set.remove(s[left])
                    left+=1
                left+=1
                
            else:
                my_set.add(s[right])
                maximumLen = max(maximumLen, len(my_set))


        return maximumLen