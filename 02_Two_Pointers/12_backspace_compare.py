# Time O(M+N) | Space O(1)
# Where M and N are the lengths of the two input strings respectively.
def backspace_compare(s, t):
    i, j = len(s) - 1, len(t) - 1
    while i >= 0 or j >= 0:
        i2 = get_next_valid_ch_index(s, i)
        j2 = get_next_valid_ch_index(t, j)
        if i2 < 0 and j2 < 0:
            return True
        if i2 < 0 or j2 < 0:
            return False
        if s[i2] != t[j2]:
            return False
        i = i2 - 1
        j = j2 - 1
    return True


def get_next_valid_ch_index(s, i):
    backspace_count = 0
    while i >= 0:
        ch = s[i]
        if ch == '#':
            backspace_count += 1
        elif backspace_count > 0:
            backspace_count -= 1
        else:
            return i
        i -= 1
    return i


def main():
    print(backspace_compare("xy#z", "xzz#"))
    print(backspace_compare("xy#z", "xyz#"))
    print(backspace_compare("xp#", "xyz##"))
    print(backspace_compare("xywrrmp", "xywrrmu#p"))


if __name__ == '__main__':
    main()
