from collections import Counter


# Time O(N) | Space O(1)
def length_of_longest_ones_subarray(nums, k):
    longest = 0
    counter = Counter()
    window_start = 0
    one_count = 0
    for window_end, digit in enumerate(nums):
        counter[digit] += 1
        if digit == 1:
            one_count += 1
        if window_end - window_start + 1 - one_count > k:
            start_digit = nums[window_start]
            counter[start_digit] -= 1
            if start_digit == 1:
                one_count -= 1
            window_start += 1
        longest = max(longest, window_end - window_start + 1)
    return longest


def main():
    print(length_of_longest_ones_subarray([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
    print(length_of_longest_ones_subarray([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))


if __name__ == '__main__':
    main()
