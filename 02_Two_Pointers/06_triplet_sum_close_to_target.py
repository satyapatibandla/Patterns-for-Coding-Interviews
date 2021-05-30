# Time O(n^2) | Space O(n)
def triplet_sum_close_to_target(arr, target_sum):
    arr.sort()
    n = len(arr)
    closest = arr[0] + arr[1] + arr[2]
    i = 0
    while i < n - 2:
        j, k = i + 1, n - 1
        while j < k:
            total = arr[i] + arr[j] + arr[k]
            if abs(target_sum - total) < abs(target_sum - closest):
                closest = total
            if total < target_sum:
                j += 1
            elif total > target_sum:
                k -= 1
            else:
                return total
        i += 1
    return closest


def main():
    print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
    print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
    print(triplet_sum_close_to_target([1, 0, 1, 1], 100))


if __name__ == '__main__':
    main()
