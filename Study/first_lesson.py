import os

# Get the path to the desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
text = "a" * 1024 * 1024
# Create 10 text files with the extension .txt
for i in range(20000):
    file_name = f"file_{i}.txt"
    file_path = os.path.join(desktop_path, file_name)
    with open(file_path, "w") as file:
        file.write(text)

print("Ничего не вышло :(.")
