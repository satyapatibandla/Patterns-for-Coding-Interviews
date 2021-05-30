# Time O(N) | Space O(1)
def dutch_flag_sort(arr):
    n = len(arr)
    left_index, right_index = 0, n - 1
    i = 0
    while i <= right_index:
        x = arr[i]
        if x == 0:
            arr[i], arr[left_index] = arr[left_index], arr[i]
            left_index += 1
        elif x == 2:
            arr[i], arr[right_index] = arr[right_index], arr[i]
            right_index -= 1
            continue
        i += 1
    return


def main():
    arr = [1, 0, 2, 1, 0]
    dutch_flag_sort(arr)
    print(arr)

    arr = [2, 2, 0, 1, 2, 0]
    dutch_flag_sort(arr)
    print(arr)


if __name__ == '__main__':
    main()
