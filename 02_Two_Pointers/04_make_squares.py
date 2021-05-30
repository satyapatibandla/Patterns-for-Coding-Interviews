# Time O(N) | Space O(N)
def make_squares(arr):
    n = len(arr)
    squares = [0 for _ in range(n)]
    left, right = 0, len(arr) - 1
    write_index = n - 1
    while left <= right:
        if abs(arr[left]) <= abs(arr[right]):
            squares[write_index] = arr[right] ** 2
            right -= 1
        else:
            squares[write_index] = arr[left] ** 2
            left += 1
        write_index -= 1
    return squares


def main():
    print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
    print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))


if __name__ == '__main__':
    main()
