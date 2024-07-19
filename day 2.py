# collections datatype 
"""
dummy_list = [] #list
enter_value = input("Enter the value:")
dummy_list.append(enter_value)
print(dummy_list)
"""
#sets
#dictnaory
"""
dummy_tuple = () #tuple
enter_value = input("Enter the value:")
dummy_tuple.append(enter_value) 
print(dummy_tuple)
"""

# basic slicing
"""
dummy_list = [1,2,3,4,5,6,7,8,9,10]
sublist = dummy_list[2:5]
print(sublist)

"""
#python sliciing with steps
"""
dummy_list = [1,2,3,4,5,6,7,8,9,10]
print(len(dummy_list))
print(dummy_list[0:10:2])# 
"""
"""
dummy_tuple = ("a", "b", "1", "2", "3")
print(dummy_tuple[2:8:2])
print(len(dummy_tuple))
print(dummy_tuple[2::])
"""

# python dictonary(day 3)

"""
students = {
    "1": "Ram", ## front=key ## back=value
    "2": "Shyam", 
}
print(students["1"])

students = {
    "11": ["Ram", "Shyam", "Hari"],
    "12": ["sita", "gita" , "Anita"]
}
print(students["11"])
"""

"""
collections = {
    "animals": ["Lion", "Dog", "Cat", "Leopard", "Goat"], 
    "birds": ["parrot", "Mainah", "sparrow", "hwak", "Eagle"],
    "mamals": {
        "name": ["bat", "human", "whale"]
        
    }

    
}
a = input("Enter the name of arial animals:")
collections.update({
    "arial": a
    


})
#print(collections)
#print(collections.update)
#print(collections["mamals"])
#print(Collections.keys())
#print(Collections.values())
#print(collections["birds"][3])
"""


## ask the 2 students their name and roll from user
# input1_name = input("Enter your name:")
# input1_rollno = input("Enter your roll no:")

# input2_name = input("Enter your name:")
# input2_rollno = input("Enter your roll no:")

# students =    {}

# students.update({
#     input1_rollno: input1_name,
#     input2_rollno: input2_name
# })
# students.update({
#     "students": [input1_name, input2_name],
#     "rollno" : [input1_rollno, input2_rollno],
# })

# print(students)

