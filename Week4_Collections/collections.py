'''
###### LISTS #######
# 1. Allow us to hold duplicate values
# 2. Order is maintained
# 3. Can hold heterogeneous data (different types of data, ints, strings, lists, etc)

list1 = [10, 'test', True, 20.24, 10]
print(list1)

## len() ---> returns the number of elements in the list
print(len(list1))

## index and slice
print(list1[2]) #accessing element at 3rd position
print(list1[1:4])
print(list1[-2])

## lists can hold other lists too
list2 = [10, 'hi', False, 2.12, ["hello", True, 20]]
print(list2)

## Creating an empty list
countries = []


# Elements can be added to a list using either append, insert, or extend methods
countries.append('USA')
countries.append('Canada')
countries.append('Mexico')
print(countries) # append always adds elements at the end

countries.insert(1, 'France')
print(countries)

countries2 = ['Germany', 'Russia', 'Italy']
countries.extend(countries2)
print(countries)

#countries.append(countries2)
#print(countries)

### Remove an element - can use either remove or pop method
countries.remove('France')
print(countries)

removed_country = countries.pop()
print(removed_country)

print(countries.pop(2)) # pop by default removes the last element but we can also specify a particular index

### Sorting lists
countries.sort() # in-place functions, modifying the internal contents of the list
print(countries)

num_list = [3434, 2193, 12, 43, 7]
num_list.sort(reverse=True)
print(num_list)

## Membership Test
print("USA" in countries)

## Creating a string from list elements
countries_str = '-'.join(countries)
print(countries_str)
print(type(countries))
print(type(countries_str))

## Creating a list by breaking string into different elements
countries3 = countries_str.split('-')
print(countries3)

#################### TUPLES ##################
# Similar to lists, but once they are created, we cannot add new elements to it, or remove any elements from it
tuple1 = (36, 45, 32, 45, 3468)
print(tuple1)  #order maintained, duplicated allowed
print(tuple1[2])

#tuple1[2] = 89    # cannot modify, add, or remove
# Can access or slice a tuple


#################### SETS ####################
# 1. Do not allow duplicate values
# 2. Order is not guranteed

courses = {'Networking', 'English', 'Math', 'English', 'History'}
print(courses)
print('Math' in courses)

### Widely used for 'set' operations
courses1 = {'Networking', 'Physics', 'Programming'}
print(courses.intersection(courses1))
print(courses.union(courses1))
print(courses.difference(courses1))
print(courses1.difference(courses))

courses.add('Psychology')
courses.remove('Math')

print(courses)

################# DICTIONARIES ##################
# store key-value pairs
employees = {
    'id': 2133,
    'name': 'Jane Doe',
    'salary': 4500,
    'skills': ['Java', 'SQL', 'C#'],
    'address': {
        'city': 'NYC',
        'state': 'NY',
        'zip-code': 12213
    }
}

## Accessing dictionary values
print(employees['name'])
print(employees['address']['city'])

employees['name'] = 'Ryan'

employees.update({'name': 'Jane Watson', 'salary': '5000'})

## Deleting Key
del employees['salary']

## Accessing keys
print(employees.get('address'))
print(employees.get('phone'))
#print(employees['phone'])  #throws error, .get does not
print(employees.get('phone', 'Not found!'))


### CREATING EMPTY COLLECTIONS ###
list1 = []
tuple1 = ()

#tuple with a single element
tuple2 = (15,)  # add a comma after the number to create it as a tuple instead of an integer
print(type(tuple2))

#set1 = {}  # this will create a dictionary
dict1 = {}
set1 = set()
'''

#### ACCESSING COLLECTION ITEMS ####
list1 = [34, 43, 65, 7, [45, 56, 20, [1234, 233, 6578]], 4]
print(list1[4][3][1])
list1[2] = 99  # modifying a value - possible for lists and tuples
list1.index(7)  # returns the position of a given value in the list
# tuples also support indexing and slicing

set1 = {34, 235, 32, 1}
#print(set1[2])  # This wont work because sets dont maintain order

dict1 = {
    'name': 'John',
    'age': 25,
    'address': {
        'city': 'Boston',
        'state': 'MA',
        'zip': 12434
    },
    'skills': ['Java', 'SQL', 'PHP']
}

print(dict1['address']['state'])

employee_details = [
    {
        'name': 'John',
        'age': 25,
        'address': {
            'city': 'Boston',
            'state': 'MA',
            'zip': 12434,
    },
        'skills': ['Java', 'SQL', 'PHP']
    },
    {
        'name': 'Jane',
        'age': 28,
        'address': {
            'city': 'Pittsburgh',
            'state': 'PA',
            'zip': 12434,
        },
        'skills': ['Java', 'SQL', 'PHP']
    }
]

#### LIST and TUPLE to a SET ####
list2 = [343, 3, 5, 8, 10, 3]
set2 = set(list2)
print(set2)