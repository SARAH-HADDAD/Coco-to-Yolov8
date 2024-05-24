import os

def replace_first_char_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        if lines:
            lines[0] = '0' + lines[0][1:]
        
        with open(file_path, 'w') as file:
            file.writelines(lines)
        
        return True
    except FileNotFoundError:
        print(f"File not found at the specified path: {file_path}")
        return False

def count_newlines_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        newline_count = content.count('\n')
        return newline_count
    except FileNotFoundError:
        print(f"File not found at the specified path: {file_path}")
        return -1

#directory_path = '/Users/sarahhaddad/Desktop/Segmentation/train/labels'
directory_path = '/Users/sarahhaddad/Desktop/Segmentation/valid/labels'

# Check if the directory exists
if os.path.exists(directory_path) and os.path.isdir(directory_path):
    txt_files = [file for file in os.listdir(directory_path) if file.endswith('.txt')]
    
    if txt_files:
        print("The directory contains the following .txt files:")
        for txt_file in txt_files:
            file_path = os.path.join(directory_path, txt_file)
            
            # Replace the first character of the first line
            if replace_first_char_in_file(file_path):
                # Count the number of newlines
                newline_count = count_newlines_in_file(file_path)
                if newline_count >= 0:
                    print(f"{txt_file}: {newline_count} newlines")
    else:
        print("The directory does not contain any .txt files.")
else:
    print("The specified directory does not exist or is not a directory.")
