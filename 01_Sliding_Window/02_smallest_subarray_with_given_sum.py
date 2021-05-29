# Time O(N) | Space O(1)
def smallest_subarray_with_given_sum(s, arr):
    smallest_length = float('inf')
    curr_sum = 0
    window_start = 0
    for window_end, num in enumerate(arr):
        curr_sum += num
        while curr_sum >= s:
            smallest_length = min(smallest_length, window_end - window_start + 1)
            curr_sum -= arr[window_start]
            window_start += 1
    return smallest_length if smallest_length != float('inf') else 0


def main():
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))


if __name__ == '__main__':
    main()
