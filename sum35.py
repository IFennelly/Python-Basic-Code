# Multiples of 3 and 5   https://projecteuler.net/problem=1
# Project Euler Problem 1
# Inez Fennelly

sum = 0
i = 1

while i < 1000:
    if i % 2 == 0:
      sum = sum + i
    elif i % 4 == 0 :
      sum = sum + i 
    i = i + 1
            
print ("Sum of multiples of 2 & 4, less than 1000 =", sum)

# Go back to see if elif is changed to "if" answer returned is diff - why?

