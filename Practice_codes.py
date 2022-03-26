# python local and global variables 

message="How are you doing?"

def greet():
    message="How are you"
    print("Inside message", message)

greet()
print("Outside message", message)