num_1 = 20
num_2 = 30
num_3 = 40


def menu():
    print("press\n a = add \n m = multiple \n d = divide \n e = exit")
def ask_user_input():
    user_input = input("select an option from menu: ")
    return user_input


def add():
        return num_1+num_2+num_3
def sub():
        return num_1-num_2-num_3
def mul():
        return num_1*num_2*num_3
def div():
        return num_1/num_2

      
if __name__=="__main__":
    menu()
    
    
    user_input = ask_user_input()
    add_output=sub_output=mul_output=div_output=0
    while "a" in ["a", "s", "m", "d", "e"]:
        if user_input == "a":
            add_output = add()
        elif user_input == "s":
            sub_output = sub()
        elif user_input == "m":
            mul_output = mul()
        elif user_input == "d":
            div_output = div()
        else:
            break
        menu()
        user_input = input("do ypu want to continue ? ")
    print(f"Result:\n Addition:{add_output}\n Subraction:{sub_output}\n multiplication:{mul_output}\n Divide:{div_output}")
    
    
    
             
            
            
        
    