from collections import Counter


# Time O(N) | Space O(1)
def length_of_longest_substring_same_after_replacement(s, k):
    max_length = 0
    window_start = 0
    max_occurring_ch_count = 0
    ch_counts = Counter()
    for window_end, end_ch in enumerate(s):
        ch_counts[end_ch] += 1
        if ch_counts[end_ch] > max_occurring_ch_count:
            max_occurring_ch_count = ch_counts[end_ch]
        while window_end - window_start + 1 - max_occurring_ch_count > k:
            start_ch = s[window_start]
            ch_counts[start_ch] -= 1
            if ch_counts[start_ch] == 0:
                del ch_counts[start_ch]
            if start_ch == max_occurring_ch_count:
                max_occurring_ch_count -= 1
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


def main():
    print(length_of_longest_substring_same_after_replacement("aabccbb", 2))
    print(length_of_longest_substring_same_after_replacement("abbcb", 1))
    print(length_of_longest_substring_same_after_replacement("abccde", 1))


if __name__ == '__main__':
    main()
