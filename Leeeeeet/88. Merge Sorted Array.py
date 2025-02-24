class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        while nums2:
            nums1[nums1.index(0)]=nums2.pop()
        nums1.sort()