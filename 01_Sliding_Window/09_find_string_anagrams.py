from collections import Counter


# Time O(N+M) | Space (M)
# Where N and M are the number of characters in the input string and the pattern, respectively.
def find_string_anagrams(s, p):
    result_indexes = []
    pattern_len = len(p)
    pattern_ch_count = Counter(p)
    ch_count = Counter()
    to_match = len(pattern_ch_count)
    matched = 0
    window_start = 0
    for window_end, end_ch in enumerate(s):
        ch_count[end_ch] += 1
        if ch_count[end_ch] == pattern_ch_count[end_ch]:
            matched += 1
        if matched == to_match:
            result_indexes.append(window_start)
        if window_end - window_start + 1 == pattern_len:
            start_ch = s[window_start]
            if ch_count[start_ch] == pattern_ch_count[start_ch]:
                matched -= 1
            ch_count[start_ch] -= 1
            window_start += 1
    return result_indexes


def main():
    print(find_string_anagrams("ppqp", "pq"))
    print(find_string_anagrams("abbcabc", "abc"))


if __name__ == '__main__':
    main()
