# filename: lesson_crud.py

import os

# create a new directory Lessons
os.makedirs(os.path.join(os.getcwd(), "Lessons"), exist_ok=True)

# Create a file readme.txt inside Lessons directory
file_path = os.path.join(os.getcwd(), "Lessons", "readme.txt")

with open(file_path, "w") as lesson_file:
    lesson_file.write("This is a readme file for the Lessons directory.\n")

# Write to the file readme.txt
with open(file_path, "a") as lesson_file:
    lesson_file.write("This is additional information about the Lessons directory.\n")

# Read the content of the file readme.txt
with open(file_path, "r") as lesson_file:
    print("File content:\n", lesson_file.read(), "\n")

# Update the file readme.txt
update_text = "This is an updated information about the Lessons directory.\n"
with open(file_path, "r+") as lesson_file:
    lesson_file.seek(0)  # move cursor to the beginning of file
    lesson_file.truncate()  # remove all content from the cursor position
    lesson_file.write(update_text)

# Read the updated content
with open(file_path, "r") as lesson_file:
    print("Updated file content:\n", lesson_file.read(), "\n")

# Delete the file
os.remove(file_path)
print("File has been deleted.")
