class Solution:
    def isValid(self, s: str) -> bool:
        myset = {"{", "(", "["}
        mystack = []

        for i in range(len(s)):
            if s[i] in myset: 
                mystack.append(s[i])
            else:
                if len(mystack) == 0:
                    return False
                c = mystack.pop()
                match s[i]:
                    case "}":
                        if c != "{": 
                            return False
                    case ")":
                        if c != "(":
                            return False
                    case "]":
                        if c != "[":
                            return False
        return len(mystack) == 0
        