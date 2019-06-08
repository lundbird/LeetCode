class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        #write backwards but all nonletters stay in place
        #two ptr technique like using C
        l,r=0,len(S)-1
        S=list(S)
        while l<r:
            if not S[l].isalpha():
                l+=1
                continue
            if not S[r].isalpha():
                r-=1
                continue
            S[l],S[r]=S[r],S[l]
            l+=1
            r-=1
        return ''.join(S)