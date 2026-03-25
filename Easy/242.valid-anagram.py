#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        string1 = list(s)
        string2 = list(t)
        sum1 = 0
        sum2 = 0 
        isAnagram = False
        
        for letter in string1:
            sum1 += ord(letter)
        
        for letter in string2:
            sum2 += ord(letter)
            
        if not (len(string1) == len(string2)):
            isAnagram = False  
        elif sum1 == sum2:
            isAnagram = True
        
        return isAnagram
# @lc code=end

