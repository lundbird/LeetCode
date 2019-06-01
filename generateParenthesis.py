class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n==1: return ["()"]
        child = self.generateParenthesis(n-1)
        res = set()
        for entry in child:
            for i in range(len(entry)):
                if entry[i]=="(":
                    new_str = "(" + entry[:i+1] + ")" + entry[i+1:]
                    res.add(new_str)
            res.add("()" + entry)
        return res