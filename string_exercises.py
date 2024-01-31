'''
#Question 1: Take an input string from the user and create a new string with the first, middle, and last characters of the input string
user_string = input("Please enter a string: ")
print(user_string)

first_char = user_string[0]
last_char = user_string[-1]

# To get the middle character, find length and index of middle character
str_length = len(user_string)
mid_index = int(str_length/2)   # since indices can only be inside of integers

mid_char = user_string[mid_index]   # To access the char at mid index

result_string = first_char + mid_char + last_char
print(result_string)


#Question 2: Take an input string from the user and create a new string made of the middle three characters of the input string
# 1st, get the input
# 2nd, use len() to find the length of the string
# 3rd, find the middle index by taking the int of the length of the string / 2
# 4th, to get the other two middle indexes, create two variables, and for one, subtract 1 from the middle index, and for the other, add 1
# 5th, add the 3 indexes and print
user_string = input("Please enter a string: ")
str_length = len(user_string)
mid_index = int(len(user_string)/2)
first_index = mid_index - 1
last_index = mid_index + 1
result_string = user_string[first_index] + user_string[mid_index] + user_string[last_index]
print(result_string)


#Question 3: Take 2 strings as inputs from the user. Append the second string in the middle of the first string
# 1st, get the two inputs
# 2nd, find the mid index by taking the int of the length of the string / 2
# 3rd, use that index to create two strings from one, one starting with it, and one ending with it
# 4th, add all 3 strings together and print it
user_string1 = input("Please enter a string: ")
user_string2 = input("Please enter another string: ")
mid_index = int(len(user_string1)/2)
first_half = user_string1[:mid_index]
second_half = user_string1[mid_index:]
result_string = first_half + user_string2 + second_half
print(result_string)


#Question 4:  Take a string from the user and reverse it
# 1st, get the input
# 2nd, use len() to find the length of the string
# 3rd, use [::-1] to flip the string around
# 4th, print the resulting string
user_string = input("Please enter a string: ")
str_length = len(user_string)
result_string = user_string[::-1]
print(result_string)


#Question 5: Extract the amount from the below string
# 1st, use .find("$") to find what index the dollar sign starts at
# 2nd, since the amount is the last part of the string, we start at the index found, and take the rest of the string with it
# 3rd, print out the amount
string = "The total value of the 10 products purchased along with the tax is $150"
starting_index = string.find("$")
amount = string[starting_index:]
print(amount)

#Question 6: Try to change the 4th character of a given string. Were you able to do it?
# 1st, get the two inputs
# 2nd, use .replace to replace the 4th character with the second input
# 3rd, print the resulting string
user_string = input("Please enter a string that is at least 4 characters long: ")
new_char = input("What would you like the 4th character to be to changed to?: ")
result_string = user_string.replace(user_string[3], new_char)
print(result_string)

first_name = input("What is your first name?: ")
last_name = input("What is your last name?: ")
age = input("What is your age?: ")
ssn = input("What is your social security number?: ")
height = float(input("What is your height in centimeters?: "))
weight = float(input("What is your weight pounds?: "))

print(f"Hello {first_name} {last_name}! Thank you for applying. Please find your details below.\n"
      f"Age: {age}\n"
      f"SSN: {ssn}\n"
      f"Height: {int(height * 0.393701)} inches\n"
      f"Weight: {int(weight * 0.453592)} kgs")


seuss = "You have brains in your head. You have feet in your shoes. You can steer yourself any direction you choose. -Dr. Seuss"

steer_start = seuss.find("steer")
steer_end = seuss.find("choose") + 7
steer_quote = seuss[steer_start:steer_end]
print(steer_quote.find("feet"))
print(steer_quote)

steer_quote = seuss[steer_start:]
steer_quote = steer_quote.replace("Dr. Seuss", "Dr. Seuss, Oh, the Places You’ll Go!")
print(steer_quote)
'''
