from collections import Counter
import heapq

class Solution:
    def isNStraightHand(self, hand, groupSize):
        if len(hand) % groupSize != 0:
            return False
        freq = Counter(hand)
        keys = sorted(freq.keys())
        heap = []
        for k in keys:
            heapq.heappush(heap, (-freq[k], k))
        for k in keys:
            while freq[k] > 0:
                temp = []
                for i in range(groupSize):
                    val = k + i
                    if freq[val] <= 0:
                        return False
                    freq[val] -= 1
                heap = []
                for key in freq:
                    if freq[key] > 0:
                        heapq.heappush(heap, (-freq[key], key))
        return True