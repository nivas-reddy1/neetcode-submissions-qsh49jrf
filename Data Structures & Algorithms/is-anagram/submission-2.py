class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS, countT = {}, {}
        for a in s:
            countS[a] = countS.get(a, 0) + 1
        for b in t:
            countT[b] = countT.get(b, 0) + 1
        
        return countS == countT