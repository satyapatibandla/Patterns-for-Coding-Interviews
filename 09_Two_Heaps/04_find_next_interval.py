import heapq


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


# Time O(N(log(N)) | Space O(N)
def find_next_interval(intervals):
    n = len(intervals)

    # heaps for finding the maximum start and end
    max_start_heap, max_end_heap = [], []

    result = [0 for _ in range(n)]
    for end_index in range(n):
        heapq.heappush(max_start_heap, (-intervals[end_index].start, end_index))
        heapq.heappush(max_end_heap, (-intervals[end_index].end, end_index))

    # go through all the intervals to find each interval's next interval
    for _ in range(n):
        # let's find the next interval of the interval which has the highest 'end'
        top_end, end_index = heapq.heappop(max_end_heap)
        result[end_index] = -1  # defaults to -1
        if -max_start_heap[0][0] >= -top_end:
            top_start, start_index = heapq.heappop(max_start_heap)
            # find the the interval that has the closest 'start'
            while max_start_heap and -max_start_heap[0][0] >= -top_end:
                top_start, start_index = heapq.heappop(max_start_heap)
            result[end_index] = start_index
            # put the interval back as it could be the next interval of other intervals
            heapq.heappush(max_start_heap, (top_start, start_index))

    return result


def main():
    result = find_next_interval([Interval(2, 3), Interval(3, 4), Interval(5, 6)])
    print("Next interval indices are: " + str(result))

    result = find_next_interval([Interval(3, 4), Interval(1, 5), Interval(4, 6)])
    print("Next interval indices are: " + str(result))


if __name__ == '__main__':
    main()
