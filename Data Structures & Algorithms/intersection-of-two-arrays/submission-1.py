class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash1 = defaultdict(set)
        arr =[]
        for i in range(len(nums1)):
            hash1[nums1[i]].add(1)
        for i in range(len(nums2)):
            hash1[nums2[i]].add(2)
        for nums , arrs in hash1.items():
            arrs = list(arrs)
            if sum(arrs) == 3:
                arr.append(nums)
        return arr
        

        