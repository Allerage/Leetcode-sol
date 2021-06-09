class Solution:
    def romanToInt(self, s: str) -> int:
        sym={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        l=len(s)-1
        res=0
        while l >=0:
            if l<len(s)-1 and sym[s[l]]<sym[s[l+1]]:
                res-=sym[s[l]]
            else:
                res+=sym[s[l]]
            l-=1
        return res  
