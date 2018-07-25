# coding : UTF-8


def reverse(text):
    return text[::-1]


def is_palindrome(text):
    print(text)
    return text == reverse(text)


something = input("Enter text: ")
# lower character
something = something.lower()
# remove all the whitespace
something = something.replace(' ', '')
if is_palindrome(something):
    print("Yes, it is a palindrome")
else:
    print("No, not a palindrome")
