class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS, countT = {}, {}
        for a in s:
            countS[a] = 1 + countS.get(a, 0)
        for b in t:
            countT[b] = 1 + countT.get(b, 0)
        return countT == countS