from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Count the frequency of elements in nums1
        freq = Counter(nums1)
        
        # Iterate through nums2 and add the common elements to the result
        result = []
        for num in nums2:
            if num in freq and freq[num] > 0:
                result.append(num)
                freq[num] -= 1
        
        return result
        