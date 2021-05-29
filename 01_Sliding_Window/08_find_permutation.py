from collections import Counter


# Time O(N+M) | Space O(M)
# Where N and M are the number of characters in the input string and the pattern, respectively.
def find_permutation(s, pattern):
    len_pattern = len(pattern)
    pattern_ch_count = Counter(pattern)
    ch_counts = Counter()
    to_match = len(pattern_ch_count)
    matched = 0
    window_start = 0
    for window_end, end_ch in enumerate(s):
        ch_counts[end_ch] += 1
        if end_ch in pattern_ch_count and ch_counts[end_ch] == pattern_ch_count[end_ch]:
            matched += 1
        if matched == to_match:
            return True
        if window_end - window_start + 1 == len_pattern:
            start_ch = s[window_start]
            if ch_counts[start_ch] == pattern_ch_count[start_ch]:
                matched -= 1
            ch_counts[start_ch] -= 1
            window_start += 1
    return False


def main():
    print('Permutation exist: ' + str(find_permutation("oidbcaf", "abc")))
    print('Permutation exist: ' + str(find_permutation("odicf", "dc")))
    print('Permutation exist: ' + str(find_permutation("bcdxabcdy", "bcdyabcdx")))
    print('Permutation exist: ' + str(find_permutation("aaacb", "abc")))


if __name__ == '__main__':
    main()
