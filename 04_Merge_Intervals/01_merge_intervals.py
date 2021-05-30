class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


# Time O(N(log(N)) | Space O(N)
def merge(intervals):
    n = len(intervals)
    if n == 0:
        return []
    intervals.sort(key=lambda i: i.start)
    merged = [intervals[0]]
    for i in range(1, n):
        interval = intervals[i]
        if merged[-1].end < interval.start:
            merged.append(interval)
        else:
            merged[-1].end = max(merged[-1].end, interval.end)
    return merged


def main():
    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
        i.print_interval()
    print()


if __name__ == '__main__':
    main()
