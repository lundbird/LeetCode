
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1*x for x in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)
            if y-x!=0:
                heapq.heappush(stones,y-x)

        return -stones[-1] if stones else 0
    def lastStoneWeight2(self, stones: List[int]) -> int:
        stones = sorted(stones)
        for _ in range(len(stones) - 1):
            x, y = stones.pop(), stones.pop()
            bisect.insort(stones, abs(x - y))
        return stones.pop()