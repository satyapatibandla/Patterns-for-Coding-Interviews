import heapq


# Time O(N*K) | Space O(K)
class SlidingWindowMedian:
    def __init__(self):
        self.top_min_heap = []
        self.bottom_max_heap = []

    def find_sliding_window_median(self, nums, k):
        result = [0.0 for _ in range(len(nums) - k + 1)]
        for i in range(0, len(nums)):
            if not self.bottom_max_heap or -self.bottom_max_heap[0] >= nums[i]:
                heapq.heappush(self.bottom_max_heap, -nums[i])
            else:
                heapq.heappush(self.top_min_heap, nums[i])

            self.balance_heaps()

            if i - k + 1 >= 0:
                if len(self.bottom_max_heap) == len(self.top_min_heap):
                    result[i - k + 1] = (-self.bottom_max_heap[0] + self.top_min_heap[0]) / 2.0
                else:
                    result[i - k + 1] = -self.bottom_max_heap[0] / 1.0

                element_to_be_removed = nums[i - k + 1]
                if element_to_be_removed <= -self.bottom_max_heap[0]:
                    self.remove(self.bottom_max_heap, -element_to_be_removed)
                else:
                    self.remove(self.top_min_heap, element_to_be_removed)

                self.balance_heaps()
        return result

    @staticmethod
    def remove(heap, element):
        ind = heap.index(element)
        heap[ind] = heap[-1]
        heap.pop()
        if ind < len(heap):
            heapq.heapify(heap)

    def balance_heaps(self):
        # either both the heaps will have equal number of elements or max-heap will have
        # one more element than the min-heap
        if len(self.bottom_max_heap) > len(self.top_min_heap) + 1:
            heapq.heappush(self.top_min_heap, -heapq.heappop(self.bottom_max_heap))
        elif len(self.bottom_max_heap) < len(self.top_min_heap):
            heapq.heappush(self.bottom_max_heap, -heapq.heappop(self.top_min_heap))


def main():
    sliding_window_median = SlidingWindowMedian()
    result = sliding_window_median.find_sliding_window_median([1, 2, -1, 3, 5], 2)
    print("Sliding window medians are: " + str(result))

    sliding_window_median = SlidingWindowMedian()
    result = sliding_window_median.find_sliding_window_median([1, 2, -1, 3, 5], 3)
    print("Sliding window medians are: " + str(result))


if __name__ == '__main__':
    main()
