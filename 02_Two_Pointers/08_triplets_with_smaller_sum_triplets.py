# Time O(N^3) | Space O(N)
def triplets_with_smaller_sum_triplets(arr, target):
    arr.sort()
    n = len(arr)
    triplets = []
    i = 0
    while i < n - 2:
        j, k = i + 1, n - 1
        while j < k:
            total = arr[i] + arr[j] + arr[k]
            if total < target:
                for k_ in range(k, j, -1):
                    triplets.append([arr[i], arr[j], arr[k_]])
                j += 1
            else:
                k -= 1
        i += 1
    return triplets


def main():
    print(triplets_with_smaller_sum_triplets([-1, 0, 2, 3], 3))
    print(triplets_with_smaller_sum_triplets([-1, 4, 2, 1, 3], 5))


if __name__ == '__main__':
    main()
