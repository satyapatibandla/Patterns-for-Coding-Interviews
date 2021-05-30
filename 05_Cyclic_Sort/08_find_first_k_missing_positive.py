# Time O(N+K) | Space O(K)
def find_first_k_missing_positive(nums, k):
    i, n = 0, len(nums)
    while i < n:
        j = nums[i] - 1
        if 0 < nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    missing_numbers = []
    extra_numbers = set()
    for i in range(n):
        if len(missing_numbers) < k:
            if nums[i] != i + 1:
                missing_numbers.append(i + 1)
                extra_numbers.add(nums[i])

    i = 1
    while len(missing_numbers) < k:
        candidate_number = i + n
        if candidate_number not in extra_numbers:
            missing_numbers.append(candidate_number)
        i += 1

    return missing_numbers


def main():
    print(find_first_k_missing_positive([3, -1, 4, 5, 5], 3))
    print(find_first_k_missing_positive([2, 3, 4], 3))
    print(find_first_k_missing_positive([-2, -3, 4], 2))


if __name__ == '__main__':
    main()
