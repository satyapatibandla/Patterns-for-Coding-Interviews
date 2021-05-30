import heapq


class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        # min heap based on meeting.end
        return self.end < other.end


# Time O(N(log(N)) | Space O(N)
def min_meeting_rooms(meetings):
    meetings.sort(key=lambda x: x.start)

    min_rooms = 0
    min_heap = []
    for m in meetings:
        while min_heap and m.start >= min_heap[0].end:
            heapq.heappop(min_heap)
        heapq.heappush(min_heap, m)
        min_rooms = max(min_rooms, len(min_heap))

    return min_rooms


def main():
    print("Minimum meeting rooms required: " +
          str(min_meeting_rooms([Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])))
    print("Minimum meeting rooms required: " +
          str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 5), Meeting(7, 9)])))
    print("Minimum meeting rooms required: " +
          str(min_meeting_rooms([Meeting(6, 7), Meeting(2, 4), Meeting(8, 12)])))
    print("Minimum meeting rooms required: " +
          str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 3), Meeting(3, 6)])))
    print("Minimum meeting rooms required: " +
          str(min_meeting_rooms([Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])))


if __name__ == '__main__':
    main()
