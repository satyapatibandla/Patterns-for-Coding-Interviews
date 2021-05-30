# Time O(N^2) | Space O(N)
def triplets_with_smaller_sum_count(arr, target):
    arr.sort()
    n = len(arr)
    count = 0
    i = 0
    while i < n - 2:
        j, k = i + 1, n - 1
        while j < k:
            total = arr[i] + arr[j] + arr[k]
            if total < target:
                count += k - j
                j += 1
            else:
                k -= 1
        i += 1
    return count


def main():
    print(triplets_with_smaller_sum_count([-1, 0, 2, 3], 3))
    print(triplets_with_smaller_sum_count([-1, 4, 2, 1, 3], 5))


if __name__ == '__main__':
    main()
