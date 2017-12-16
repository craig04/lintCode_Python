class Solution:
    """
    @param: nums1: an integer array
    @param: nums2: an integer array
    @return: an integer array
    """

    def intersection(self, nums1, nums2):
        dict1 = dict()
        for n in nums1:
            dict1[n] = dict1.setdefault(n, 0) + 1
        intersection = []
        for n in nums2:
            if n in dict1 and dict1[n] != 0:
                intersection.append(n)
                dict1[n] -= 1
        return intersection
