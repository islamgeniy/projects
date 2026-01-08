def linear_search(arr, x, location):
    i=1
    while i <= n and x != arr[i]:
        i = i + 1
    if i <= n: 
        location[0] = i
    else:
        location[0] = 0 
    
    return location

# Example usage:
arr = [0, 3, 5, 2, 4]  # Note: arr[0] is unused
x = 2 # Element to search for
n = 4 # Length of the array
location = [0] # Using a list to hold the location as a mutable object
result = linear_search(arr, x, location)
print("Element found at location:", result[0])  # Output: Element found at location: 3