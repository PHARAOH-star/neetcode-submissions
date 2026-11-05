
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hm = {}

        # Step 1: Count frequency
        for num in nums:
            hm[num] = hm.get(num, 0) + 1

        # Step 2: Sort by frequency
        sorted_nums = sorted(hm, key=hm.get, reverse=True)

        # Step 3: Return top k
        return sorted_nums[:k]
