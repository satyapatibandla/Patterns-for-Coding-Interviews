import heapq


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


class EmployeeInterval:
    def __init__(self, interval, employee_index, interval_index):
        self.interval = interval
        self.employee_index = employee_index
        self.interval_index = interval_index

    def __lt__(self, other):
        return self.interval.start < other.interval.start


# Time O(N(log(K)) | Space O(K)
# where N is the total number of intervals, and K is the total number of employees
def find_employee_free_time(schedule):
    if not schedule:
        return []

    result, min_heap = [], []

    n = len(schedule)
    for i in range(n):
        heapq.heappush(min_heap, EmployeeInterval(schedule[i][0], i, 0))

    previous_interval = min_heap[0].interval
    while min_heap:
        curr = heapq.heappop(min_heap)

        if curr.interval.start > previous_interval.end:
            result.append(Interval(previous_interval.end, curr.interval.start))
            previous_interval = curr.interval
        else:
            if previous_interval.end < curr.interval.end:
                previous_interval = curr.interval

        emp_schedule = schedule[curr.employee_index]
        if curr.interval_index + 1 < len(emp_schedule):
            heapq.heappush(min_heap, EmployeeInterval(emp_schedule[curr.interval_index + 1],
                                                      curr.employee_index,
                                                      curr.interval_index + 1))

    return result


def main():
    print("Free intervals: ", end='')
    for interval in find_employee_free_time([[Interval(1, 3), Interval(5, 6)], [Interval(2, 3), Interval(6, 8)]]):
        interval.print_interval()
    print()

    print("Free intervals: ", end='')
    for interval in find_employee_free_time([[Interval(1, 3), Interval(9, 12)], [Interval(2, 4)], [Interval(6, 8)]]):
        interval.print_interval()
    print()

    print("Free intervals: ", end='')
    for interval in find_employee_free_time([[Interval(1, 3)], [Interval(2, 4)], [Interval(3, 5), Interval(7, 9)]]):
        interval.print_interval()
    print()


if __name__ == '__main__':
    main()
