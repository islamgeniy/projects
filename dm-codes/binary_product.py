def multiply(a, b):
    """
    Multiply two positive integers represented in binary.
    a and b are lists of bits: [a_0, a_1, ..., a_{n-1}]
    Returns the product p
    """
    n = max(len(a), len(b))
    
    # Pad with zeros to make equal length
    a_padded = a + [0] * (n - len(a))
    b_padded = b + [0] * (n - len(b))
    
    p = 0
    
    for j in range(n):
        if b_padded[j] == 1:
            # c_j = a shifted j places left
            c_j = binary_to_decimal(a_padded) << j
            p = p + c_j
    
    return p


def binary_to_decimal(bits):
    """Convert binary representation (list of bits) to decimal."""
    return sum(bit * (2**i) for i, bit in enumerate(bits))


def decimal_to_binary(n):
    """Convert decimal to binary representation (list of bits)."""
    if n == 0:
        return [0]
    bits = []
    while n > 0:
        bits.append(n & 1)
        n >>= 1
    return bits


# Example usage:
# 5 in binary is [1, 0, 1] (101 in binary)
# 3 in binary is [1, 1] (011 in binary)
# 5 * 3 = 15
a = [1, 0, 1]  # 5
b = [1, 1]      # 3
result = multiply(a, b)
print(f"Binary product: {result} (decimal)")  # Output: 15

a_decimal = binary_to_decimal(a)
b_decimal = binary_to_decimal(b)
print(f"{a_decimal} * {b_decimal} = {result}")  # Output: 5 * 3 = 15

# More examples
a2 = [0, 1]  # 2
b2 = [1, 1]  # 3
result2 = multiply(a2, b2)
print(f"{binary_to_decimal(a2)} * {binary_to_decimal(b2)} = {result2}")  # Output: 2 * 3 = 6
