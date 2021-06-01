# Time O(N*2^N) | Space O(N*2^N)
def find_subsets_with_duplicates(nums):
    nums.sort()
    subsets = [[]]
    start_index, end_index = 0, 0
    for i in range(len(nums)):
        start_index = 0
        if i > 0 and nums[i] == nums[i - 1]:
            start_index = end_index + 1
        end_index = len(subsets) - 1
        for j in range(start_index, end_index + 1):
            subsets.append(subsets[j] + [nums[i]])
    return subsets


def main():
    print("Here is the list of subsets: " + str(find_subsets_with_duplicates([1, 3, 3])))
    print("Here is the list of subsets: " + str(find_subsets_with_duplicates([1, 5, 3, 3])))


if __name__ == '__main__':
    main()
