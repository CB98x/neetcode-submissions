class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        #create dict frequency map
        dict_chr = {}
        for chr in nums:
            dict_chr[chr] = dict_chr.get(chr, 0) +1
        #use heap to keep k and return
        heap= []
        heapq.heapify(heap)
        for num, feq in dict_chr.items():
            heapq.heappush(heap, (feq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        #create result and return
        result = []
        for chr in heap:
            feq, num = chr
            result.append(num)

        return result

