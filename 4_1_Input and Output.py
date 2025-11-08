# Ask for user inputs
name = input("Enter your name: ")
greeting = input("Enter your preferred greeting: ")

# Combine using an f-string
message = f"{greeting},{name}!"

# Display the custom message
print(message)