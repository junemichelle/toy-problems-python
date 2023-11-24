def convert_to_12hour (hour, minute, period): 
    # conditional statement to check the period 
    if period == "pm" and hour != 12: # if its pm and the hour is not 12,12 is added to the hour.
        hour += 12
    elif period == "am" and hour == 12: #  If it's "am" and the hour is 12, the hour is set to 0.
        hour = 0
    return "{:02}{:02}".format(hour, minute)  # using the format function to return the time in correct format. 

print(convert_to_12hour(6,12,"am"))
print(convert_to_12hour(7,16,"pm"))

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


def add_consonants(word):
    letters= "abcdefghijklmnopqrstuvwxyz" 
    values = [i+1 for i in range(26)] # iterating each letter in the input words.
    value_dict = dict(zip(letters, values)) #dictionary that maps each consonant to its value.
 
    vowels = "aeiou"
    total = 0
    max_value = 0

    for letter in word:
        if letter in vowels:
            total = 0  # Reset total when a vowel is encountered
        else:
            total += value_dict[letter]
            max_value = max(max_value, total)

    return max_value # returns totall maximum value. 


print(add_consonants("zebra")) # 26
  
