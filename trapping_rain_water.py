class Solution:
    def trap(self, height: List[int]) -> int:
        #using brute force algorithm:
        
        if not height: 
            return 0
        
        left_maxes = [height[0]]*(len(height))
        for i in range(1,len(height)):
            left_maxes[i] = max(left_maxes[i-1],height[i])
            
        right_maxes = [height[-1]]*(len(height))
        for i in range(len(height)-2,-1,-1):
            right_maxes[i] = max(right_maxes[i+1],height[i])
        
        ans = 0
        for i in range(1,len(height)-1):
            ans += max(0,(min(left_maxes[i],right_maxes[i])-height[i]))
        return ans