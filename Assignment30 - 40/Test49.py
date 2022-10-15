import os

path = os.getcwd()
print("Current Directory", path)

print(os.path.abspath(os.path.join(path, os.pardir)))