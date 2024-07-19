# # class and objects ()

# class Electronic:
#     operating_system = 'windows'
#     ram = None
#     hard_disk = None
    
#     def __init__(self, ram, hard_disk): # dunded method # this is constructor yo call hunxa jaba hamle object initialize garxam
#         print("hi i am called")
        
#         self.ram = ram
#         self.hard_disk = hard_disk
    
#     def get_ram(self):
#         return self.ram

# laptop = Electronic(4, 500) 

# laptop.get_ram()
 
# print(laptop.operating_system)
# print(laptop.ram)
# print(laptop.hard_disk)    
    
    
# class Instution: 
#     inst_name = 'collages Nepal'
#     inst_location = 'putalisadak, kathmandu' 
    
#     def __init__(self, inst_name, inst_location):
#         self.inst_name = inst_name
#         self.inst_location = inst_location
#     def get_inst_name(self):
#         return self.inst_name
#     def get_inst_location(self):
#         return self.inst_location    
# a = Instution() # error

# a.get_inst_name()
# a.get_inst_location()
# result_1 = a.get_inst_name
# result_2 = a.get_inst_location


# print(result_1)
# print(result_2)    
        
    


class Institution: 
    inst_name = 'Colleges Nepal'
    inst_location = 'Putalisadak, Kathmandu' 
    
    def __init__(self, inst_name, inst_location):
        self.inst_name = inst_name
        self.inst_location = inst_location

    def get_inst_name(self):
        return self.inst_name

    def get_inst_location(self):
        return self.inst_location

# Instantiate the class with proper arguments
a = Institution('Colleges Nepal', 'Putalisadak, Kathmandu')

# Call methods to get results
result_1 = a.get_inst_name()
result_2 = a.get_inst_location()

print(result_1)
print(result_2)
    
    