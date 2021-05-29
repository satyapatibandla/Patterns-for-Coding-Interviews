from collections import Counter


# Time O(N) | Space O(K)
def longest_substring_with_k_distinct(s, k):
    counter = Counter()
    longest = 0
    window_start = 0
    for window_end, ch in enumerate(s):
        counter[ch] += 1
        while len(counter) > k:
            start_ch = s[window_start]
            counter[start_ch] -= 1
            if counter[start_ch] == 0:
                del counter[start_ch]
            window_start += 1
        longest = max(longest, window_end - window_start + 1)
    return longest


def main():
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))


if __name__ == '__main__':
    main()
