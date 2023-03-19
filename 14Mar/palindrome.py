def is_palindrome(n):
    return str(n) == str(n)[::-1]
def nearest_palindrome(n):
    if is_palindrome(n):
        pass
        #return n
    i = 1
    while True:
        if is_palindrome(n + i):
            return n + i
        elif is_palindrome(n - i):
            return n - i
        i += 1
n=int(input())
#print(is_palindrome(n))
print(nearest_palindrome(n+1))