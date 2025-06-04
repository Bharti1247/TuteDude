# Ask user for input
user_input = input("Enter the content to write into the file: ")

# Write the user input to the file
with open("sample.txt", "w") as file:
    file.write(user_input)