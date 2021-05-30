# Time O(N^2) | Space O(N)
def search_triplets(arr):
    n = len(arr)
    arr.sort()
    triplets = []
    i = 0
    while i < n - 2:
        if arr[i] > 0:
            break
        j, k = i + 1, n - 1
        while j < k:
            total = arr[i] + arr[j] + arr[k]
            if total < 0:
                j += 1
                while j < k and arr[j] == arr[j - 1]:
                    j += 1
            elif total > 0:
                k -= 1
                while j < k and arr[k] == arr[k + 1]:
                    k -= 1
            else:
                triplets.append([arr[i], arr[j], arr[k]])
                j += 1
                k -= 1
                while j < k and arr[j] == arr[j - 1]:
                    j += 1
                while j < k and arr[k] == arr[k + 1]:
                    k -= 1
        i += 1
        while i < len(arr) - 2 and arr[i] == arr[i - 1]:
            i += 1
    return triplets


def main():
    print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
    print(search_triplets([-5, 2, -1, -2, 3]))


if __name__ == '__main__':
    main()
