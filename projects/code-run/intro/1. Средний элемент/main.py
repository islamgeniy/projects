import sys


def main():
    
    nums = list(map(int, input().split()))
    nums.sort()              # 1. Sort the array
    mid = len(nums) // 2     # 2. Find the middle index
    print(nums[mid])
    


if __name__ == '__main__':
    main()