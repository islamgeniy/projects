def add(a, b):
    """
    Add two positive integers represented in binary.
    a and b are lists of bits: [a_0, a_1, ..., a_{n-1}]
    Returns the sum s as [s_0, s_1, ..., s_n]
    """
    n = max(len(a), len(b))
    
    # Pad with zeros to make equal length
    a_padded = a + [0] * (n - len(a))
    b_padded = b + [0] * (n - len(b))
    
    s = []
    c = 0  # carry
    
    for j in range(n):
        d = (a_padded[j] + b_padded[j] + c) // 2
        s_j = a_padded[j] + b_padded[j] + c - 2 * d
        s.append(s_j)
        c = d
    
    # Add final carry
    s.append(c)
    
    return s


# Example usage:
# 5 in binary is [1, 0, 1] (101 in binary)
# 3 in binary is [1, 1] (011 in binary)
# 5 + 3 = 8 = [0, 0, 0, 1] (1000 in binary)
a = [1, 0, 1]  # 5
b = [1, 1]      # 3
result = add(a, b)
print(f"Binary sum: {result}")  # Output: [0, 0, 0, 1] represents 1000 in binary (8 in decimal)

# Verify by converting to decimal
def binary_to_decimal(bits):
    return sum(bit * (2**i) for i, bit in enumerate(bits))

a_decimal = binary_to_decimal(a)
b_decimal = binary_to_decimal(b)
result_decimal = binary_to_decimal(result)
print(f"{a_decimal} + {b_decimal} = {result_decimal}")
