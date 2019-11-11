def is_palindrome(s):
    print(s)
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False


a = input("Enter something: ")
if is_palindrome(a) == True:
    print("Input is a palindrome!")
else:
    print("Input isn't a palindrome!")

