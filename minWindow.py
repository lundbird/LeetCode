class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def contains(outer, inner) -> bool:
            for o in inner:
                try:
                    outer.remove(o)
                except:
                    return False
            return True
        t, s = list(t), list(s)
        l,r = 0, 0
        min_window_value = math.inf
        min_window = ""
        while r<=len(s):
            window = s[l:r]
            # print(window, contains(list(s),t))
            if contains(s[l:r],t):
                if r-l < min_window_value:
                    min_window_value = r-l
                    min_window = window
                l += 1
            else:
                r += 1
        return ''.join(min_window)
    
    
    
    
            # S = "ADOBECODEBANC", T = "ABC"
#         A
#         AD
#         ADO
#         ADOB
#         ADOBE
#         ADOBEC /
#          BOBEC
#          BOBECO
#          BOBECOD
#          BOBECODE
#          BOBECODEB
#          BOBECODEBA /
#           OBECODEBA /
#            BECODEBA /
#             ECODEBA /
#              CODEBA /
#               ODEBA
#               ODEBAN
#               ODEBANC /
#                DEBANC / 
#                 EBANC /
#                  BANC /
#                   ANC 
                    
                
            
         
