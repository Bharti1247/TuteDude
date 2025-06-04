# Ask user for input
user_input = input("Enter the file name to read: ")

with open(user_input, "r") as file:
    content = file.read()
    print(content)