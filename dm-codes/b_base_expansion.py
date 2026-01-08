
def base_expansion(n, b):
    """
    Construct base b expansion of n (where b > 1)
    Returns the digits a_k-1, ..., a_1, a_0 and the count k
    """
    q = n
    k = 0
    a = []
    
    while q != 0:
        a.append(q % b)
        q = q // b
        k = k + 1
    
    # Reverse to get a_k-1, ..., a_1, a_0
    return a[::-1], k 

# Example usage:
n = 45
b = 3
digits, count = base_expansion(n, b)
print(f"Base {b} expansion of {n} is: {digits} with {count} digits")  # Output: Base 3 expansion of 45 is: [1, 2, 0, 0] with 4 digits