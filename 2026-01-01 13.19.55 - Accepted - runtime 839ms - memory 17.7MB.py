class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        n = len(s)
        count = 0
        
        for i in range(n):
            v = 0  # vowel count
            c = 0  # consonant count
            for j in range(i, n):
                if s[j] in vowels:
                    v += 1
                else:
                    c += 1
                
                if v == c and (v * c) % k == 0:
                    count += 1
        
        return count