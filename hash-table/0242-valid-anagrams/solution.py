from collections import Counter 

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        freq = Counter(s)
        for symbol in t:
            freq[symbol] -= 1
            if freq[symbol] < 0:
                return False
        return True

        # Alternative short solution
        # return Counter(s) == Counter(t)

if __name__=="__main__":
    sol = Solution()
    print(sol.isAnagram(s="anagram", t="naragam"))
