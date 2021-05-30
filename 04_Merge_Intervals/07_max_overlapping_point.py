import heapq


# Time O(N(log(N)) | Space O(N)
def max_overlapping_point(intervals):
    min_heap = []
    for start, end in intervals:
        heapq.heappush(min_heap, (start, 1))
        heapq.heappush(min_heap, (end, -1))

    max_overlap = curr_overlap = 0
    res = min_heap[0][0]
    while min_heap:
        point, change = heapq.heappop(min_heap)
        curr_overlap += change
        if curr_overlap > max_overlap:
            max_overlap = curr_overlap
            res = point

    return res


def main():
    intervals = [[-3, 5], [0, 2], [8, 10], [6, 7]]
    print("A point with the maximum overlap is: " + str(max_overlapping_point(intervals)))


if __name__ == '__main__':
    main()
