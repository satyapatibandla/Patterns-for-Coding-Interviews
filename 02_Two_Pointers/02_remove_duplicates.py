# Time O(N) | Space O(1)
def remove_duplicates(nums):
    if len(nums) <= 1:
        return len(nums)

    write_index = 1
    i = 1
    while i < len(nums):
        if nums[i - 1] != nums[i]:
            nums[write_index] = nums[i]
            write_index += 1
        i += 1

    return write_index


def main():
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates([2, 2, 2, 11]))


if __name__ == '__main__':
    main()
