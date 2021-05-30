from collections import deque


# Time O(N^3) | Space O(N^3)
def find_smaller_product_subarrays(nums, target):
    if target <= 1:
        return []
    n = len(nums)
    result = []
    product = 1
    left = 0
    for right in range(n):
        product *= nums[right]
        while product >= target:
            product /= nums[left]
            left += 1
        temp_list = deque([])
        for i in range(right, left - 1, -1):
            temp_list.appendleft(nums[i])
            result.append(list(temp_list))
    return result


def main():
    print(find_smaller_product_subarrays([2, 5, 3, 10], 30))
    print(find_smaller_product_subarrays([8, 2, 6, 5], 50))


if __name__ == '__main__':
    main()
