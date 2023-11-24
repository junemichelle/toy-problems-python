def check_two_positive(a, b, c):
    #  if statement to check if each of the three numbers a, b, and c is greater than zero.
    count = 0
    if a > 0:
        count += 1 # if the numbers is greater than 0 the count variable is incremented by 1.
    if b > 0:
        count += 1 
    if c > 0:
        count += 1
    return count == 2 # returns true if the count is equal to 2 i.e 2 of the 3 numbers are positive 
                      # it returs false otherwise.

print(check_two_positive(2, 4, -3))   # True
print(check_two_positive(-4, 6, 8))   # True
print(check_two_positive(4, -6, 9))   # True
print(check_two_positive(-4, 6, 0))   # False
print(check_two_positive(4, 6, 10))   # False
