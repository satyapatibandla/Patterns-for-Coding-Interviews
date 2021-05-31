import heapq


class MedianOfAStream:
    # Space O(N)
    def __init__(self):
        self.top_min_heap = []
        self.bottom_max_heap = []

    # Time O(log(N))
    def insert_num(self, num):
        if not self.bottom_max_heap or -self.bottom_max_heap[0] >= num:
            heapq.heappush(self.bottom_max_heap, -num)
        else:
            heapq.heappush(self.top_min_heap, num)
        if len(self.bottom_max_heap) > len(self.top_min_heap) + 1:
            heapq.heappush(self.top_min_heap, -heapq.heappop(self.bottom_max_heap))
        elif len(self.top_min_heap) > len(self.bottom_max_heap):
            heapq.heappush(self.bottom_max_heap, -heapq.heappop(self.top_min_heap))

    # Time O(1)
    def find_median(self):
        if len(self.top_min_heap) == len(self.bottom_max_heap):
            return (self.top_min_heap[0] + -self.bottom_max_heap[0]) / 2
        return -self.bottom_max_heap[0] / 1.0


def main():
    median_of_a_stream = MedianOfAStream()
    median_of_a_stream.insert_num(3)
    median_of_a_stream.insert_num(1)
    print("The median is: " + str(median_of_a_stream.find_median()))
    median_of_a_stream.insert_num(5)
    print("The median is: " + str(median_of_a_stream.find_median()))
    median_of_a_stream.insert_num(4)
    print("The median is: " + str(median_of_a_stream.find_median()))


if __name__ == '__main__':
    main()
