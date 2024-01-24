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
'''

# Accessing string characters
emp_name = "Jane Doe"
print(emp_name[3])
#print(emp_name[8])  # throws index out of bounds error because the last character is at index 7

print(emp_name.index('n'))
