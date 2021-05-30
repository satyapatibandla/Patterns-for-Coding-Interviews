# Time O(N) | Space O(1)
def find_missing_numbers_1_n(nums):
    i, n = 0, len(nums)
    while i < n:
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    missing_numbers = []
    for i in range(n):
        if nums[i] != i + 1:
            missing_numbers.append(i + 1)

    return missing_numbers


def main():
    print(find_missing_numbers_1_n([2, 3, 1, 8, 2, 3, 5, 1]))
    print(find_missing_numbers_1_n([2, 4, 1, 2]))
    print(find_missing_numbers_1_n([2, 3, 2, 1]))


if __name__ == '__main__':
    main()
