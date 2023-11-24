# Toy Problems

This repository contains Python solutions for three coding challenges related to time conversion, number positivity, and consonant values.

## contains the following tasks

-  Converting 12-hour time to 24-hour time
-  Checking if two numbers are positive.
-  displaying the greatest value of consecutive consonants in a word.


## Challenge 1: Converting 12-hour time to 24-hour time

  ### Instructions
   Define a function convert_to_24_hour(hour, minute, period) that takes an hour (in the range of 1 to 12, inclusive), a minute (in the range of 0 to 59, inclusive), and a period ("am" or "pm") as input. Return a four-digit string that encodes that time in 24-hour format.
  
  ### Notes
   - By convention, noon is 12:00 pm, and midnight is 12:00 am.
   - On the 12-hour clock, there is no 0 hour. Time just after midnight  is denoted, for example, as 12:15 am. On the 24-hour clock, this translates to 0015.


## Challenge 2: Two numbers are positive.

  ### Task 

   Write a function are_exactly_two_positive(a, b, c) that takes three integers a, b, and c as arguments and returns True if exactly two of the three integers are positive numbers (greater than zero), and False otherwise.

  ### Examples

   (4, -6, 9) == True
   (-4, 6, 0) == False
   (4, 6, 10) == False


## Challenge 3: Consonant value

 Given a lowercase string that has alphabetic characters only and no spaces, return the highest value of consonant substrings. Consonants are any letters of the alphabet except "aeiou". We shall assign the following values: a = 1, b = 2, c = 3, .... z = 26.


  ### Examples
   For the word "zodiacs", solve("zodiacs") returns 26.
   For example, for the word "zodiacs", let's cross out the vowels. We get: "z d cs". The consonant substrings are: "z", "d" and "cs". The values are z = 26, d = 4, and cs = 3 + 19 = 22. The highest is 26.


## Project Setup

To set up the project locally, follow these steps:

1. Clone the repository.
2. Navigate to the project directory.
3. Create a virtual environment.
4. Activate the virtual environment.

## Author
Michelle JUne Chemutai.

## License 
For information about the license please go to the license file,  [LICENSE].