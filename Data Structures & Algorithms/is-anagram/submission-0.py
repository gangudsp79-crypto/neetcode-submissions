class Solution:
    def isAnagram(self, s, t):
        dict1,dict2={},{}
        if len(s)!=len(t):
            return False
        else:
            for i in range(len(s)):
                
                dict1[s[i]]=1+dict1.get(s[i],0)
                dict2[t[i]]=1+dict2.get(t[i],0)
                
            for c in dict1:
                if dict1[c]!=dict2.get(c,0):
                    return False
            return True


        