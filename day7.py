## multiplication table
"""
input_num = int(input("enter the num:"))
for i in range(1,11):
    print(f"{input_num}x{i}={i*input_num}")
"""
## break and continue
"""
for i in range(1,10):
    print(i)
    if i == 5:
        break
print("executed")
"""
## continue
"""
for i in range(1,10):
    if i == 5:
        continue
    print(i)
"""
"""
name = []
for i in range(1,10):
    user_input = input("enter the name:")
    a = input("do you want to continue ?")
    if a == "n":

        break
    else:                    
        name.append(user_input)
   
"""



total = 0
for i in range(1,3):
    num = int(input("enter the num:"))
    a = input("do you want to proceed or skip or break?")
    total += num
    if a == "p":
        print("proceed")
    elif a == "c":
        
        continue
        
    else:
        break
print("Total",total)  






