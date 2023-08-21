import os

# Get the current working directory
current_directory = os.getcwd()
print("Current directory:", current_directory)

# Create a new directory
new_directory = os.path.join(current_directory, "new_folder")
os.mkdir(new_directory)
print("New directory created:", new_directory)

# Change the working directory
os.chdir(new_directory)
print("Changed directory:", os.getcwd())

# Create a new file in the current directory
new_file_path = os.path.join(os.getcwd(), "example.txt")
with open(new_file_path, "w") as f:
    f.write("Hello, world!")

print("New file created:", new_file_path)

# List the contents of the current directory
directory_contents = os.listdir(os.getcwd())
print("Directory contents:", directory_contents)

# Remove the created file
os.remove(new_file_path)
print("File removed:", new_file_path)

# Change back to the original directory
os.chdir(current_directory)
print("Changed back to original directory:", os.getcwd())

# Remove the created directory
os.rmdir(new_directory)
print("Directory removed:", new_directory)
