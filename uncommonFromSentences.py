from collections import Counter
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        words = (A+" "+B).split()
        return [k for k,v in Counter(words).items() if v==1]