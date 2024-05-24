import os

def check_files_in_directory(directory_path):
    txt_files = [file for file in os.listdir(directory_path) if file.endswith('.txt')]
    
    for txt_file in txt_files:
        file_path = os.path.join(directory_path, txt_file)
        
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # Check if the file starts with '0' and has only one line
        if not lines or lines[0][0] != '0' or len(lines) != 1:
            print(f"{txt_file} does not meet the criteria")

# Specify the directory path
directory_path = '/Users/sarahhaddad/Desktop/Segmentation/labels/val'

# Check if the directory exists
if os.path.exists(directory_path) and os.path.isdir(directory_path):
    check_files_in_directory(directory_path)
else:
    print("The specified directory does not exist or is not a directory.")
