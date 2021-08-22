def is_isogram(xword):
    lst = []
    for i in xword:
        if i in lst:
            return False
        lst = lst +[i]
    return True

words = ["dermatoglyphics","palindrome", "anagram"]

for w in words:
    print(is_isogram(w))
