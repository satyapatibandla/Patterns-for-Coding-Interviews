# Time O(log(N)) | Space O(1)
def find_happy_number(num):
    slow = num
    fast = get_next(num)
    while fast != 1 and slow != fast:
        slow = get_next(slow)
        fast = get_next(get_next(fast))
    return fast == 1


def get_next(n):
    total = 0
    while n > 0:
        n, d = divmod(n, 10)
        total += d ** 2
    return total


def main():
    print(find_happy_number(23))
    print(find_happy_number(12))


if __name__ == '__main__':
    main()
