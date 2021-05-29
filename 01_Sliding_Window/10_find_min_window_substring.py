from collections import Counter


# Time O(N+M) | Space O(M)
# Where N and M are the number of characters in the input string and the pattern, respectively.
def find_min_window_substring(s, t):
    min_length = len(s) + 1
    min_window_start, min_window_end = 0, 0
    t_ch_frequency = Counter(t)
    ch_frequency = Counter()
    to_match = len(t_ch_frequency)
    matched = 0
    window_start = 0
    for window_end, end_ch in enumerate(s):
        ch_frequency[end_ch] += 1
        if ch_frequency[end_ch] == t_ch_frequency[end_ch]:
            matched += 1
        while matched == to_match:
            curr_length = window_end - window_start + 1
            if curr_length < min_length:
                min_window_start, min_window_end = window_start, window_end
                min_length = curr_length
            start_ch = s[window_start]
            if ch_frequency[start_ch] == t_ch_frequency[start_ch]:
                matched -= 1
            ch_frequency[start_ch] -= 1
            window_start += 1
    return s[min_window_start:min_window_end + 1] if min_length <= len(s) else ""


def main():
    print(find_min_window_substring("aabdec", "abc"))
    print(find_min_window_substring("abdbca", "abc"))
    print(find_min_window_substring("adcad", "abc"))


if __name__ == '__main__':
    main()
