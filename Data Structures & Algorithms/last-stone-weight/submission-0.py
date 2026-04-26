class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones ]
        heap = stones
        heapq.heapify(stones) #max heap, with negative values

        while len(heap) > 1:
            x = -1 * heapq.heappop(stones)
            y = -1 * heapq.heappop(stones)
            heapq.heappush(heap, -1*(x-y))
        
        return heap[0] * -1
        

            

        
        
        