def is_palindrome(x: int) -> bool:
    # Negative numbers and numbers ending in 0 (except 0 itself) are not palindromes
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    # Reverse half of the number
    reversed_half = 0
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10  # Reduce the original number

    # A number is a palindrome if the first half equals the reversed second half
    return x == reversed_half or x == reversed_half // 10

# Example usage
print(is_palindrome(121))   # Output: True
print(is_palindrome(-121))  # Output: False
print(is_palindrome(10))    # Output: False
