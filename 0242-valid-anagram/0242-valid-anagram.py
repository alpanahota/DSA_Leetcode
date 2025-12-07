class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(t)==len(s):
            list1=sorted(t.lower())
            list2=sorted(s.lower())
            return list1==list2
        return False