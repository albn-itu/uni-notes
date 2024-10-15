def longest_odd_palindrome(S):
    n = len(S)
    p = 10**9 + 7  # A large prime
    r = 31         # Base

    # Precompute hash values
    prefix_hash = [0] * (n + 1)
    suffix_hash = [0] * (n + 1)
    rpow = [1] * (n + 1)
    for i in range(n):
        prefix_hash[i + 1] = (prefix_hash[i] * r + ord(S[i])) % p
        suffix_hash[i + 1] = (suffix_hash[i] * r + ord(S[n - i - 1])) % p
        rpow[i + 1] = (rpow[i] * r) % p

    print(len(prefix_hash))
    print(len(prefix_hash))
    print(n, n**2)

    def is_palindrome(left, right):
        # Calculate hashes of left and right halves
        hash_left = (prefix_hash[right] -
                     prefix_hash[left] * rpow[right - left]) % p
        hash_right = (suffix_hash[n - left] -
                      suffix_hash[n - right] * rpow[right - left]) % p
        # Reverse the hash of the right half
        hash_right = (hash_right * rpow[right - left]) % p
        return hash_left == hash_right

    max_length = 1
    for i in range(n):
        # Binary search for the maximum length
        low = 0
        high = min(i, n - i - 1)
        while low <= high:
            mid = (low + high) // 2
            if is_palindrome(i - mid, i + mid + 1):
                max_length = max(max_length, 2 * mid + 1)
                low = mid + 1
            else:
                high = mid - 1

    return max_length


# Example usage
S = "ABABBABABBAAB"
print(longest_odd_palindrome(S))  # Output: 9
