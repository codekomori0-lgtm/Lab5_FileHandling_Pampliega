# Create and Write to a File 
from pathlib import Path 
 
student_id = "TUPM-25-0703" 
student_name = "Ram Anthony Esmane Pampliega" 
 
documents_path = Path.home() / "Documents" / "Activity_5_Files" 
documents_path.mkdir(parents=True, exist_ok=True) 
 
file_path = documents_path / f"i=ntro_{student_id}.txt" 
file_path.write_text(f"Welcome {student_name} (ID: {student_id}) to File Handling in Python!") 
 
print(f"File created and text written at: {file_path}")

# Read File Content 
from pathlib import Path 
 
student_id = "TUPM-25-0703" 
 
documents_path = Path.home() / "Documents" / "Activity_5_Files"  
file_path = documents_path / f"intro_{student_id}.txt" 
 
content = file_path.read_text() 
print(content) 

# Append to a File 
from pathlib import Path 
 
student_id = "TUPM-25-0703" 
 
file_path = Path.home() / "Documents" / "Activity_5_Files" / f"intro_{student_id}.txt" 
 
with file_path.open("a") as f: 
    f.write("\nThis is a new line.") 
print(f"Line appended to: {file_path}")

 # Read File Line by Line 
from pathlib import Path 
 
student_id = "TUPM-25-0703" 
 
file_path = Path.home() / "Documents" / "Activity_5_Files" / f"lines_{student_id}.txt" 
 
with file_path.open("r") as f: 
    for line in f: 
        print(line.strip())

        # Count Words in File 
from pathlib import Path 
 
student_id = "TUPM-25-0703" 
student_name = "Ram Anthony Esmane Pampliega" 
 
file_path = Path.home() / "Documents" / "Activity_5_Files" / f"lines_{student_id}.txt" 
 
text = file_path.read_text() 
word_count = len(text.split()) 
 
print(f"{student_name} (ID: {student_id}) - Word count in file '{file_path.name}': {word_count}") 

#Cell 1: Create and Write to a File 
from pathlib import Path 
 
student_id = "2025-XXXX" 
student_name = "Your Full Name" 
 
documents_path = Path.home() / "Documents" / "Activity_5_Files" 
documents_path.mkdir(parents=True, exist_ok=True) 
 
file_path = documents_path / f"intro_{student_id}.txt" 
file_path.write_text(f"Welcome {student_name} (ID: {student_id}) to File Handling in Python!") 
 
print(f"File created and text written at: {file_path}") 
 
#Cell 2: Copy File 
import shutil 
from pathlib import Path 
 
student_id = "TUPM-25-0703" 
student_name = "Ram Anthony Esmane Pampliega" 
documents_path = Path.home() / "Documents" / "Activity_5_Files" 
 
# Define source and destination 
src = documents_path / f"intro_{student_id}.txt" 
dst = documents_path / f"intro_copy_{student_id}.txt" 
 
# Copy file 
shutil.copy(src, dst) 
print(f"File copied successfully from {src.name} to {dst.name}.") 

# Rename File 
from pathlib import Path 
 
# Personal details (keep consistent per activity) 
student_id = "TUPM-25-0703" 
 
# Define directory path 
documents_path = Path.home() / "Documents" / "Activity_5_Files" 
 
# Define old and new file paths 
old_file = documents_path / f"intro_copy_{student_id}.txt" 
new_file = documents_path / f"intro_renamed_{student_id}.txt" 
 
# Rename file 
old_file.rename(new_file) 
print(f"File renamed successfully from {old_file.name} to {new_file.name}.") 

# Delete File 
from pathlib import Path 
 
# Personal details 
student_id = "TUPM-25-0703" 
 
# Define file path 
documents_path = Path.home() / "Documents" / "Activity_5_Files" 
file_path = documents_path / f"intro_renamed_{student_id}.txt" 
 
# Check and delete file if it exists 
if file_path.exists(): 
    file_path.unlink() 
    print(f"File deleted successfully from: {file_path}") 
else: 
    print(f"No file found to delete at: {file_path}") 