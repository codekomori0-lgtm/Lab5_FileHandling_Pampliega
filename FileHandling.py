# Step 1: Import Path from pathlib 
from fileinput import filename
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


#2. Reading from a File 
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


#3. Appending Data 
# Step 1: Open file in append mode 

user_text = input("Enter something to add: ")
                                        
lines = [
    "\n--- New Entries ---",
    f"\nUser said: {user_text}",
    "\nEnd of entry."
]

with open(file_path, "a", encoding="utf-8") as file:
    file.writelines(lines)

# Step 2: Confirm that data was added 
print("All data appended successfully.")


#4. Safe File Operations with Backup 
# Step 1: Import additional libraries 
from pathlib import Path
from datetime import datetime
import shutil

# Define working directory
backup_dir = Path.home() / "Documents" / "Surname_Activity_5"
backup_dir.mkdir(exist_ok=True)

# Function: Write with backup (overwrite or append)
def write_with_backup(filename: str, content: str, mode="w"):
    file_path = backup_dir / filename

    # Create backup if file exists
    if file_path.exists():
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = file_path.with_name(
            f"{file_path.stem}_YourSurname_backup_{timestamp}{file_path.suffix}"
        )
        shutil.copy2(file_path, backup_path)
        print(f"Backup saved: {backup_path.name}")

    # Write or append
    with open(file_path, mode, encoding="utf-8") as file:
        if mode == "a":
            file.write("\n" + content)
        else:
            file.write(content)

    print(f"File saved: {file_path.name}")


# Function: Read full file
def read_file(filename: str):
    file_path = backup_dir / filename
    if file_path.exists():
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    return "File does not exist."


# Function: Read line by line + word count + filter "Python"
def read_lines_with_filter(filename: str):
    file_path = backup_dir / filename

    if file_path.exists():
        with open(file_path, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, 1):
                words = line.split()
                if "Python" in line:
                    print(f"Line {line_number}: {line.strip()} ({len(words)} words)")


# Function: List backups for a file
def list_backups(filename: str):
    stem = Path(filename).stem
    backups = backup_dir.glob(f"{stem}_*backup*")

    print(f"Backups for {filename}:")
    for backup in backups:
        print("-", backup.name)


# ================= DEMO =================
print("=== File Operations Demo ===")

# 1. Create file
print("\n1. Creating new file:")
write_with_backup("demo.txt", "Hello, Welcome to Python Programming!\nPython makes file handling easy!")

# 2. User input + choose mode
print("\n2. Add content:")
choice = input("Overwrite (w) or Append (a)? ").lower()
text = input("Enter text: ")
write_with_backup("demo.txt", text, mode=choice)

# 3. Read full file
print("\n3. File content:")
print(read_file("demo.txt"))

# 4. Read filtered lines
print("\n4. Lines containing 'Python':")
read_lines_with_filter("demo.txt")

# 5. List backups
print("\n5. Backup files:")
list_backups("demo.txt")
    

#5. Menu-Driven File Manager
from pathlib import Path
from datetime import datetime
import shutil

# Step 2: Define your custom working directory
backup_dir = Path.home() / "Documents" / "Surname_Activity_5"
backup_dir.mkdir(exist_ok=True)

# Step 3: Define the menu-driven file manager
def file_manager():
    file_name = input("Enter filename (e.g., notes.txt): ")
    file_path = backup_dir / file_name

    while True:
        print("\n--- MENU ---")
        print("1. Write to file")
        print("2. Append to file")
        print("3. Read file")
        print("4. Backup file")
        print("5. List backup files")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            content = input("Enter content to write:\n")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            print("File written successfully.")

        elif choice == "2":
            more = input("Enter content to append:\n")
            with open(file_path, "a", encoding="utf-8") as f:
                f.write("\n" + more)
            print("Content appended.")

        elif choice == "3":
            if file_path.exists():
                with open(file_path, "r", encoding="utf-8") as f:
                    print("\nFile Content:\n", f.read())
            else:
                print("File not found.")

        elif choice == "4":
            if file_path.exists():
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                backup_file = file_path.with_name(
                    f"{file_path.stem}_YourSurname_backup_{timestamp}{file_path.suffix}"
                )
                shutil.copy2(file_path, backup_file)
                print(f"Backup created: {backup_file.name}")
            else:
                print("Cannot backup. File does not exist.")

        elif choice == "5":
            print("\nBackup files:")
            backups = backup_dir.glob(f"{file_path.stem}_*backup*")
            found = False
            for backup in backups:
                print("-", backup.name)
                found = True
            if not found:
                print("No backups found.")

        elif choice == "6":
            print("Exiting the file manager.")
            break

        else:
            print("Invalid choice. Please try again.")


# Step 4: Run the program
if __name__ == "__main__":
    file_manager()
