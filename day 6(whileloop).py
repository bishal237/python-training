appended_numbers = []
user_input = input("Enter the numbers:")

while user_input.isdigit():
    user_input = input("Enter the number:")
    appended_numbers.append(user_input)

print(appended_numbers)

