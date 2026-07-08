class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = defaultdict(int)
        for num in nums: # O(n)
            dict1[num] += 1
        #naive method will be to sort dict1.values()
        arr = [[] for _ in range(len(nums))] # O(n)
        for i , val in dict1.items():
            arr[val-1].append(i)
        ans = [0]*k
        j = 0
        for i in range(len(arr) -1 , -1 ,-1): # O(n)
            if arr[i] != [] and j < k: #O(1)
                while arr[i] and j < k:
                    ans[j] = arr[i].pop()
                    j = j + 1
        print(arr)
        return (ans)
        
        

        
        