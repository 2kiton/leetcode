class Solution(object):
    def scoreOfString(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        # (Letter - LetterAfter) + (LetterAfter - LetterAfterAfter) ...
        firstL = 0
        nextL = 1
        lastL = len(s)
        score = 0
        
        while firstL < lastL-1:
            score += abs(ord(s[firstL]) - ord(s[nextL]))
            nextL += 1
            firstL += 1
        else:
            return score