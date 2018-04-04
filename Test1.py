def collatz (n):
    while n > 1:
        if n % 2:
            n = 3 * n + 1
        else: 
            n /= 2
        return n
    for i in collatz (6) :
        return i
