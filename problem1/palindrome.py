
def is_palindrome(val:int) -> bool:
    str_val = str(val)
    y = len(str_val) - 1
    if y == 0:
        return True

    x = 0
    while True:
        if str_val[x] != str_val[y]:
            return False
        x += 1
        y -= 1
        if x >= y:
            return True
