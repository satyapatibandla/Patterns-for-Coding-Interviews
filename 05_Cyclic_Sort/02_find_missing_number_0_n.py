# Time O(N) | Space O(1)
def find_missing_number_0_n(nums):
    i, n = 0, len(nums)
    while i < n:
        j = nums[i]
        if nums[i] < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(n):
        if nums[i] != i:
            return i

    return n


def main():
    print(find_missing_number_0_n([4, 0, 3, 1]))
    print(find_missing_number_0_n([8, 3, 5, 2, 4, 6, 0, 1]))


if __name__ == '__main__':
    main()
