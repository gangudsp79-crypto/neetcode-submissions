class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(s)<len(t):
            return ""
        
        countT={}
        window={}
        
        
        for ch in t:
            countT[ch]=countT.get(ch, 0)+1
        left=0
        need=len(countT)
        have=0
        res=""
        res_len=float("inf")
        for right in range(len(s)):
            char=s[right]
            window[char]=window.get(char, 0)+1
            if char in countT and window[char]==countT[char]:
                have+=1
            while have==need:
                if (right-left+1)<res_len:
                    res=s[left:right+1]
                    res_len=right-left+1
                window[s[left]]-=1
                if s[left] in countT and window[s[left]]<countT[s[left]]:
                    have-=1
                left+=1
        return res


            
        