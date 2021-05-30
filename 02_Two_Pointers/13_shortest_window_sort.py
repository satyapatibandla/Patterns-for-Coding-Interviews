# Time O(N) | Space O(1)
def shortest_window_sort(arr):
    n = len(arr)
    left, right = 0, n - 1

    while left < n - 1 and arr[left] <= arr[left + 1]:
        left += 1
    if left == n - 1:
        return 0

    while right > 0 and arr[right] >= arr[right - 1]:
        right -= 1

    sub_min = float('inf')
    sub_max = float('-inf')
    for k in range(left, right + 1):
        sub_min = min(sub_min, arr[k])
        sub_max = max(sub_max, arr[k])

    while left > 0 and arr[left - 1] > sub_min:
        left -= 1

    while right < n - 1 and arr[right + 1] < sub_max:
        right += 1

    return right - left + 1


def main():
    print(shortest_window_sort([1, 2, 5, 3, 7, 10, 9, 12]))
    print(shortest_window_sort([1, 3, 2, 0, -1, 7, 10]))
    print(shortest_window_sort([1, 2, 3]))
    print(shortest_window_sort([3, 2, 1]))


if __name__ == '__main__':
    main()
