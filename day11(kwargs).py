#kwargs


def greet(name, age,**kwargs):
    print(kwargs)

greet(name = "bishal", age = 12)







def get_email(email):
    if "@" in email:
        return True
    else:
        
        return False

Results = get_email(email= "abcd@gmail.com")
print(Results)

"""
def get_email(email):
    if "@" in email:
        return True
    else:
        return False
get_userinput = input("Enter your email: ")
results = get_email(email =[])
   """ 



