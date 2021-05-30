# Time O(N) | Space O(1)
def remove_element(arr, key):
    write_index = 0

    for i in range(len(arr)):
        if arr[i] != key:
            arr[write_index] = arr[i]
            write_index += 1

    return write_index


def main():
    print("Array new length: " + str(remove_element([3, 2, 3, 6, 3, 10, 9, 3], 3)))
    print("Array new length: " + str(remove_element([2, 11, 2, 2, 1], 2)))


if __name__ == '__main__':
    main()
