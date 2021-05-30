# Time O(N) | Space O(N)
def insert_interval(intervals, new_interval):
    result = []
    i, start, end = 0, 0, 1
    while i < len(intervals) and intervals[i][start] < new_interval[start]:
        result.append(intervals[i])
        i += 1

    while i < len(intervals) and intervals[i][start] <= new_interval[end]:
        new_interval[start] = min(new_interval[start], intervals[i][start])
        new_interval[end] = max(new_interval[end], intervals[i][end])
        i += 1

    result.append(new_interval)

    while i < len(intervals):
        result.append(intervals[i])
        i += 1

    return result


def main():
    print("Intervals after inserting the new interval: " + str(insert_interval([[1, 3], [5, 7], [8, 12]], [4, 6])))
    print("Intervals after inserting the new interval: " + str(insert_interval([[1, 3], [5, 7], [8, 12]], [4, 10])))
    print("Intervals after inserting the new interval: " + str(insert_interval([[2, 3], [5, 7]], [1, 4])))


if __name__ == '__main__':
    main()
