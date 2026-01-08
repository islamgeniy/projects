def binary_search(arr, target):
    """
    Perform binary search on a sorted array to find the index of the target value.

    Parameters:
    arr (list): A list of sorted elements.
    target: The value to search for in the list.

    Returns:
    int: The index of the target value if found, otherwise -1.
    """
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2

        # Check if target is present at mid
        if arr[mid] == target:
            return mid
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        # If target is smaller, ignore right half
        else:
            right = mid - 1

    # Target was not found in the array
    return "not found"

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
result = binary_search(arr, target)
print("Element " + str(target) + " found at index:", result)  # Output: Element 5 found at index: 4