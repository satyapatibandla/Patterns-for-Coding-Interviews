# Time O(N) | Space O(1)
def non_repeat_substring(s):
    max_length = 0
    window_start = 0
    last_seen_index = {}
    for window_end, ch in enumerate(s):
        if ch in last_seen_index:
            window_start = max(window_start, last_seen_index[ch] + 1)
        max_length = max(max_length, window_end - window_start + 1)
        last_seen_index[ch] = window_end
    return max_length


def main():
    print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abccde")))


if __name__ == '__main__':
    main()
