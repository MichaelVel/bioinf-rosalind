import os

# Set the directory name
dir_name = "workspace"

# Create the workspace directory
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
    print(f"Directory {dir_name} created.")

# Create the subdirectories
subdirs = ["foo", "bar"]
for subdir in subdirs:
    subdir_path = os.path.join(dir_name, subdir)
    if not os.path.exists(subdir_path):
        os.mkdir(subdir_path)
        print(f"Subdirectory {subdir_path} created.")

# Create the test.py file
file_path = os.path.join(dir_name, "test.py")
with open(file_path, "w") as file:
    file.write("print('Hello, World!')\n")
    print(f"File {file_path} created.")

