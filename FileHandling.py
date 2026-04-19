# Step 1: Import Path from pathlib 
from pathlib import Path 

# Step 2: Define a custom folder in your Documents directory 
output_dir = Path.home() / "Documents" / "PythonFiles" 
output_dir.mkdir(exist_ok=True)  # Creates folder if missing 

# Step 3: Define the file path 
file_path = output_dir / "Surname_Activity_5" 

# Step 4: Write text to the file 
with open(file_path, "w", encoding="utf-8") as file: 
    file.write("Hello, Welcome to Python Programming!\n") 
    file.write("File saved safely with pathlib.") 
    file.write("Python makes file handling easy!")


# Step 5: Confirm that the file is saved 
print(f"File saved to: {file_path.resolve()}")


# Step 1: Read the entire file content if it exists 
if file_path.exists(): 
    with open(file_path, "r", encoding="utf-8") as file: 
        content = file.read() 
print("File content:\n", content) 

# Step 2: Read line-by-line 
with open(file_path, "r", encoding="utf-8") as file:
    for line_number, line in enumerate(file, 1):
        words = line.split()
        print(f"Line {line_number} has {len(words)} words.")