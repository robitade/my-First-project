class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Convert the arrays to sets to remove duplicates
        set1 = set(nums1)
        set2 = set(nums2)
        
        # Find the intersection of the two sets
        intersection = set1.intersection(set2)
        
        # Convert the intersection set back to a list and return it
        return list(intersection)
        