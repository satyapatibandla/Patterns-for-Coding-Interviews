# Time O(N) | Space O(1)
def circular_array_loop_exists(nums):
    for i in range(len(nums)):
        if nums[i] == 0:
            continue

        direction = nums[i] > 0

        slow = fast = i
        while True:
            slow = get_next_idx(nums, slow, direction)
            fast = get_next_idx(nums, get_next_idx(nums, fast, direction), direction)

            if slow == -1 or fast == -1:
                break

            elif slow == fast:
                return True

        slow = i
        while get_next_idx(nums, slow, direction) != -1:
            temp_slow = slow
            slow = get_next_idx(nums, slow, direction)
            nums[temp_slow] = 0

    return False


def get_next_idx(nums, idx, direction):
    if idx == -1:
        return -1
    elif (nums[idx] > 0) != direction:
        return -1
    next_idx = (idx + nums[idx]) % len(nums)
    return -1 if next_idx == idx else next_idx


def main():
    print(circular_array_loop_exists([1, 2, -1, 2, 2]))
    print(circular_array_loop_exists([2, 2, -1, 2]))
    print(circular_array_loop_exists([2, 1, -1, -2]))


if __name__ == '__main__':
    main()
