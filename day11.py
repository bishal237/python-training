#Arbitary list of arguments 
#args, kwargs

"""
def  get_square(*number):
    print(number)

get_square(10,11,12)
"""
"""
def get_name(*names):
    user_name = []
    for name in names:
        user_name.append(len(name))
    return user_name
    
    
    

result = get_name("Bishal", "sandesh", "saroj")
print(result)
""" 

#kwargs

def greet(name = "Alex", **kwargs):
    pass

greet(name = "bishal", age = 12)
    