# Inez Fennelly 7th March 2018
# Fizz Buzz https://en.wikipedia.org/wiki/Fizz_buzz

i = 1

while i <= 30:
    if (i % 3 == 0) and (i % 5 == 0):
        print ("Fizz Buzz")
    elif i % 3 == 0:
        print ("Fizz")
    elif i % 5 == 0:
        print ("Buzz")
    else:
        print (i)
    i = i + 1
