def palindrome(x):
    # String starts from left->right
    left=str(x)
    # String starts from rightl->left
    right=x[::-1]
    return left == right

print(palindrome("aba"))
print(palindrome("a"))
print(palindrome("abba"))
print(palindrome("amanaplanacanalpanama"))
print(palindrome("abca"))
print(palindrome("ac"))
print(palindrome("adabbba"))
print(palindrome("amandaplanacanalpanama"))
