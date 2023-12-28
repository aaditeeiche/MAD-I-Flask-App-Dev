import sys

print("This is the hello.py file")
# name = input("Enter your name: ")

print("Total Parameters:", len(sys.argv))
print("First Parameter:", int(sys.argv[1]), type(int(sys.argv[1])))
print("Second Parameter:", sys.argv[2], type(sys.argv[2]))
