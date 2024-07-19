## function
"""
def greet():
    print("hello")
    return "abcd"

result = greet()
print(result)
"""
## functions with argument
"""
def greet_with_name(name):# name is required argument
    return f"hello, {name}"
result = greet_with_name("Bishal")
print(result)
"""
## greet with default arguments

def greet_with_name(name = "Alex"): # default argument
    return f"hello , {name}"

result  =greet_with_name()
print(result)


# .................

