import random
import sys
import os

long_string = "I'll catch you if you fall - The Floor"

print(long_string[0:4]) #till 4 digits in string
print(long_string[-5:]) #starts from last
print(long_string[:-5])
print(long_string[:4] + " meet you up") #concatenation of two strings

print("%c is my %s letter and my number %d number is %.5f " %('X','favorite',1 , .14))

# Returns true if all characters are letters ' isn't a letter
print(long_string.isalpha())

# Returns true if all characters are numbers
print(long_string.isalnum())

# Returns the string length
print(len(long_string))

# Replace the first word with the second (Add a number to replace more)
print(long_string.replace("Floor", "Ground"))

# Remove white space from front and end
print(long_string.strip())

# Split a string into a list based on the delimiter you provide
quote_list = long_string.split(" ")
print(quote_list)