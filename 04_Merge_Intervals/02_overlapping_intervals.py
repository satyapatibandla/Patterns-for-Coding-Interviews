class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return "[" + str(self.start) + ", " + str(self.end) + "]"


# Time O(N(log(N)) | Space O(N)
def has_overlap(intervals):
    n = len(intervals)
    intervals.sort(key=lambda i: i.start)
    for i in range(1, n):
        if intervals[i].start <= intervals[i - 1].end:
            return True
    return False


def main():
    intervals = [Interval(1, 4), Interval(2, 5), Interval(7, 9)]
    print(intervals)
    print("Overlapping Intervals: ", end='')
    print(has_overlap(intervals))


if __name__ == '__main__':
    main()
