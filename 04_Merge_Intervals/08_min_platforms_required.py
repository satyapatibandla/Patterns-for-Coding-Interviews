import heapq


# Time O(N(log(N)) | Space O(N)
def min_platforms_required(arr, dep):
    min_heap = []
    for a, d in zip(arr, dep):
        heapq.heappush(min_heap, (a, 1))
        heapq.heappush(min_heap, (d, -1))

    max_overlap = curr_overlap = 0
    while min_heap:
        _, change = heapq.heappop(min_heap)
        curr_overlap += change
        if curr_overlap > max_overlap:
            max_overlap = curr_overlap

    return max_overlap


def main():
    arr = [900, 940, 950, 1100, 1500, 1800]
    dep = [910, 1200, 1120, 1130, 1900, 2000]
    print("Minimum Number of Platforms Required: " + str(min_platforms_required(arr, dep)))


if __name__ == '__main__':
    main()
