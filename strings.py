# Adding a comment in the remote repo
'''
print("Hello World")
# For variable names, don't use reserved keywords
print(help('keywords'))

# Assign multiple variables with the same value simultaneously
a = b = c = 10  # works but not recommended
print(a, b, c)

# Expression vs Statement
x = 47  # Statement (simply declaring a variable)
y = 47 + 10  # Expression (evaluating/processing something)

# Type Conversion
# Converting to int
print(int(10.24))
print(int(float("10.24")))

# Convert to string
print(str(20))
print(type(str(20)))

print(list("hello"))

# Strings
# Can be created either by using single, double, or triple quotes
first_name = 'Jane'
print(first_name)

last_name = "Doe"
print(last_name)

address = "10 Main St"
print(address)

job1 = "Physician's Assistant"
print(job1)

# String Functions
emp_name = "Jane Doe"
# len() --> returns the number of characters in a given string
print(len(emp_name))

# upper and lower --> these convert the string into corresponding cases
print(emp_name.upper())

# String concatenation
first_name = "Jane"
last_name = "Doe"
print(first_name + " " + last_name)

age = 24
print(first_name + ' ' + last_name + ': ' + str(age))

# String Multiplication
print('Hello'*3)
# Can only add two strings, and can only multiple a string with an int

# Accessing string characters
emp_name = "Jane Doe"
print(emp_name[3])
#print(emp_name[8])  # throws index out of bounds error because the last character is at index 7

print(emp_name.index('n'))
'''

# String Slicing
emp_name = "Jane Doe"
print(emp_name[2:6])
print(emp_name[:4])     #start from the beginning and go until the third index
print(emp_name[5:])     #start from 5 and go through the rest of the indeces
print(emp_name[-4:-1])  #negative values go backwards, last index is -1, the second to last -2, etc
print(emp_name[1:6:2])  #step value, returns every other index

print(emp_name.count('e'))  #Counts how many 'e' are in the string
print(emp_name.find('Doe')) #Finds the index at which 'Doe' starts
emp_name = emp_name.replace('Jane', 'John') #Replaces some part of the string with something else
print('oh' in emp_name) #Membership test, finds if something is in the list/string

#String Formatting
student_name = 'Alice'
score = 87

print(student_name + ':', score)
print("Name: {} Score: {}".format(student_name, score))

#f-strings
print(f'Name: {student_name} Score: {score}')
print(f'10 times 3 is {10*3}')