class Solution:
   def containsNearbyDuplicate(self, nums, k):
    # Create a dictionary to store the elements and their indices
    num_dict = {}
    
    for i, num in enumerate(nums):
        # If the current element is already in the dictionary
        # and the difference between the current index and the previous index is less than or equal to k
        if num in num_dict and abs(i - num_dict[num]) <= k:
            return True
        
        # Update the dictionary with the current element and its index
        num_dict[num] = i
    
    return False