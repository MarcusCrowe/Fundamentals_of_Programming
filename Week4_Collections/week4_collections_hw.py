# Q1
tuple1 = ("Car", [34, 23, 8], False, [15, 20, 11])
print(tuple1[3][1])

# Q2
List1 = [44, 12, 578, 21, 134, 67]
print(List1[3:])

#Q3
list1 = [5, 10, 15, 20, 75, 100, 50]
index = list1.index(20)
list1[index] = 200
print(list1)

#Q4
tuple1 = (11, [64, 33], 243, 123)
tuple1[1][1] = 66
print(tuple1)

#Q5
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3 = set1.union(set2)
print(set3)

#Q6 - NOT FINISHED
list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
list3 = []
list3.extend(list1[1::2])
list3.extend(list2[0::2])
print(list3)


#Q7
list1 = [34, 54, 67, 89, 11, 43, 94]
popped_element = list1.pop(4)
list1.insert(2, popped_element)
list1.append(popped_element)
print(list1)

#Q8
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)

#Q9
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
list2 = ["h", "i", "j"]
list1[2][1][2].extend(list2)
print(list1)

#Q10
Tuple1 = (40, 19, 234, 12, 10, 123)
Tuple1 = Tuple1[::-1]
print(Tuple1)

#Q11
dict1 = {
    "course": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

print(dict1["course"]["student"]["marks"]["history"])