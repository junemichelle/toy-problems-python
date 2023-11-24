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
  
