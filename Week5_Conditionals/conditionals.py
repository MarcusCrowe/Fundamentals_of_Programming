### if-else
'''
height = int(input("What is your height?: "))

if height > 120:
    print("You can ride")

else:
    print('You cannot ride')


### nested if-else
height = int(input("What is your height?: "))

if height > 120:
    print("You can ride")
    age = int(input("\nWhat is your age?: "))
    if age > 18:
        print('The cost is: $12')
    else:
        print('The cost is: $7')

else:
    print('You cannot ride')

### nested elif
height = int(input("What is your height?: "))

if height > 120:
    print("You can ride")
    age = int(input("\nWhat is your age?: "))
    if age > 45 and age < 55:
        cost = 0

    elif age > 18:
        cost = 12

    elif age >= 12 and age < 18:
        cost = 7

    else:
        cost = 5

    print(f'The cost is: ${cost}')

    want_photos = input("Do you want a photo taken? Enter Y/y or N/n: ")
    if want_photos == "y" or want_photos == "Y":
        cost = cost + 3

    print(f'The cost is: ${cost}')
else:
    print('You cannot ride')

### Grade Calculator
grade = int(input("What is the grade?: "))

if grade < 60:
    print('F')
elif grade < 70:
    if grade < 63:
        print('D-')
    if grade < 67:
        print("D")
    else:
        print("D+")
elif grade < 80:
    if grade < 73:
        print("C-")
    elif grade < 77:
        print("C")
    else:
        print("C+")
elif grade < 90:
    if grade < 83:
        print("B-")
    elif grade < 87:
        print("B")
    else:
        print("B+")
elif grade <= 100:
    if grade < 93:
        print("A-")
    elif grade < 97:
        print("A")
    else:
        print("A+")
else:
    print("Invalid input.")
'''

#Ask user to enter a digit between 0 and 9
#Return the corresponding word
#EX) user enters 1 --> program returns 'One'

digit = int(input("Enter a number 0 to 9: "))

num_list = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
if digit >= 0 and digit <= 9:
    print(num_list[digit])
else:
    print('Invalid number!')
