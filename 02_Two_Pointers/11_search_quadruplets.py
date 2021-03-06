# Time O(N^3) | Space O(N)
def search_quadruplets(arr, target):
    arr.sort()
    quadruplets = []
    for i in range(len(arr) - 3):
        if i and arr[i] == arr[i - 1]:
            continue
        for j in range(i + 1, len(arr) - 2):
            if j > i + 1 and arr[j] == arr[j - 1]:
                continue
            search_pairs(arr, target, i, j, quadruplets)
    return quadruplets


def search_pairs(arr, target_sum, first, second, quadruplets):
    left = second + 1
    right = len(arr) - 1
    while left < right:
        quad_sum = arr[first] + arr[second] + arr[left] + arr[right]
        if quad_sum < target_sum:
            left += 1
            while left < right and arr[left] == arr[left - 1]:
                left += 1
        elif quad_sum > target_sum:
            right -= 1
            while left < right and arr[right] == arr[right + 1]:
                right -= 1
        else:
            quadruplets.append([arr[first], arr[second], arr[left], arr[right]])
            left += 1
            while left < right and arr[left] == arr[left - 1]:
                left += 1
            right -= 1
            while left < right and arr[right] == arr[right + 1]:
                right -= 1


def main():
    print(search_quadruplets([4, 1, 2, -1, 1, -3], 1))
    print(search_quadruplets([2, 0, -1, 1, -2, 2], 2))


if __name__ == '__main__':
    main()
