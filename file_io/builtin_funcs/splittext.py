import os

filename = "example.txt"
name, extension = os.path.splitext(filename)

print("File name:", name)
print("Extension:", extension)
