class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t)<len(s):
            return False
        ind=list()
        for i in range(len(s)):
            if s[i] not in t:

                return False
            try :
                ind.append(t.index(s[i]))
                print(ind[-1])
                if len(ind)>1:
                    if ind[-1]<=ind[-2]:
                        return False 
            except:
                return False

        if len(ind)==len(s):
            return True
c=Solution()
c.isSubsequence(input(),input())
