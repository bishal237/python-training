## files

"""
1. r-> read
2. w-> write 
3. a-> append
4. r+ -> read and write
5. b-> binary(bytes)
"""

# f = open("python.py", "w")
# f.write("hello world")



# with statemenet ()

# for i in range(1,10):
#     with  open("students_Info.txt", "a") as f:
#         f.write(f"student name: Ram \t Roll no :{i} \t class: 12\n")


with open("students_Info.txt", "r") as f:
    print(f.read())
    