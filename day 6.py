# # # # # # loop statements

# # # # # ## for loop

# # # # # my_list = [1,2,3,4,5,6,7,8,9]
# # # # # my_tuple = (1,2,3,4,5,6,7,8,9,)
# # # # # my_dict = {
# # # # #     "a": 1,
# # # # #     "b": 2
# # # # # }
# # # # # for i in my_list:
# # # # #     print(i)

# # # # # for i in range(1,9):
# # # # #     print(i)


# # # # # for key, value in my_dict.items():
# # # # #     print(key)
# # # # #     print(value)


# # # # my_list = [1, 2, 3, 4, 5]
# # # # for i in my_list:
# # # #     print(i)

# # # ##students = {
# # #     "ram": 90
# # #     "hari": 80
# # # }
# # # total = 0
# # # for key, value in students.items():
# # #     total = total + value
# # #     print(total)
    
# # students = {"name": "rajesh", "math": 60, "science": 70}
# # new_dict = {}
# # total = 0

# # for key, value in students.items():
# #     if key != "name":  # Ensure we only add numeric values to total
# #         total += value

# # new_dict = students.copy()  # Copy existing dictionary
# # new_dict["total"] = total   # Add total to new dictionary

# # print(new_dict)

# score_1 = {
#     "alice": 80,
#     "bob": 75
# }

# scores_2 = {
#     "charlie": 85,
#     "david": 90
# }
# combined_dict = {**score_1,  ** scores_2}
# print(combined_dict)

