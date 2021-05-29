# Time O(N) | Space O(1)
def pair_with_targetsum(arr, target_sum):
    left, right = 0, len(arr) - 1
    while left < right:
        total = arr[left] + arr[right]
        if total < target_sum:
            left += 1
        elif total > target_sum:
            right -= 1
        else:
            return [left, right]
    return [-1, -1]


def main():
    print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
    print(pair_with_targetsum([2, 5, 9, 11], 11))


if __name__ == '__main__':
    main()
