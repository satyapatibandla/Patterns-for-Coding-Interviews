from collections import Counter


# Time O(N) | Space O(1)
def fruits_into_baskets(fruits):
    counter = Counter()
    longest = 0
    window_start = 0
    for window_end, end_fruit in enumerate(fruits):
        counter[end_fruit] += 1
        while len(counter) > 2:
            start_fruit = fruits[window_start]
            counter[start_fruit] -= 1
            if counter[start_fruit] == 0:
                del counter[start_fruit]
            window_start += 1
        longest = max(longest, window_end - window_start + 1)
    return longest


def main():
    print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
    print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))


if __name__ == '__main__':
    main()
