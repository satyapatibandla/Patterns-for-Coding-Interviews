# Time O(N*2^N) | Space O(N*2^N)
def find_subsets(nums):
    subsets = [[]]
    for num in nums:
        for i in range(len(subsets)):
            subsets.append(subsets[i] + [num])
    return subsets


def main():
    print("Here is the list of subsets: " + str(find_subsets([1, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


if __name__ == '__main__':
    main()
