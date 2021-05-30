import heapq


class Job:
    def __init__(self, start, end, cpu_load):
        self.start = start
        self.end = end
        self.cpu_load = cpu_load


# Time O(N(log(N)) | Space O(N)
def find_max_cpu_load(jobs):
    min_heap = []
    for j in jobs:
        heapq.heappush(min_heap, (j.start, j.cpu_load))
        heapq.heappush(min_heap, (j.end, -j.cpu_load))

    curr_load = max_load = 0
    while min_heap:
        time, load_change = heapq.heappop(min_heap)
        curr_load += load_change
        if curr_load > max_load:
            max_load = curr_load

    return max_load


def main():
    print("Maximum CPU load at any time: " + str(find_max_cpu_load([Job(1, 4, 3), Job(2, 5, 4), Job(7, 9, 6)])))
    print("Maximum CPU load at any time: " + str(find_max_cpu_load([Job(6, 7, 10), Job(2, 4, 11), Job(8, 12, 15)])))
    print("Maximum CPU load at any time: " + str(find_max_cpu_load([Job(1, 4, 2), Job(2, 4, 1), Job(3, 6, 5)])))


if __name__ == '__main__':
    main()
