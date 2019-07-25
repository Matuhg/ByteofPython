def reverse(text):
    return text[::-1]


forbiddenchars = ('.', ',', '!', '?', ':')


# for loop is used to remove punctuation.
def is_palindrome(text):
    for c in text:
        text = text.replace(c, '')
    return text == reverse(text)


something = input("Enter text: ")
if is_palindrome(something):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")

