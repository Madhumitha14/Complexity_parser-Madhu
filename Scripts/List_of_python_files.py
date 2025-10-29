import os

def list_python_files(directory):
    python_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))
    return python_files


project_directory = "C:/Users/DELL/robotframework"
python_files = list_python_files(project_directory)

#print the full path of Python files to the command prompt
for file in python_files:
    print(file)

#Saving the list of Python file paths to a text file
with open("python_files_list.txt", "w")as file:
    for python_file in python_files:
        file.write(python_file + "\n")

#print number of Python files in directories
num_python_files = len(python_files)
print(f"Number of Python files: {num_python_files}")