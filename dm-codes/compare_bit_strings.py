def compare_bit_strings(P, Q, n):
    """
    Compare two bit strings P and Q of length n and return the number of differing bits.
    
    Parameters:
    P (str or list of int): First bit string (e.g., "10101" or [1,0,1,0,1])
    Q (str or list of int): Second bit string
    n (int): Length of the bit strings
    
    Returns:
    int: Number of positions where P and Q differ
    """
    d = 0
    for i in range(n):
        if P[i] != Q[i]:
            d += 1
    return d

# Example usage:
P = "1111"
Q = "1100"
n = 4
print(compare_bit_strings(P, Q, n))  # Output: 2