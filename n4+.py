import os

print("hi<3 this is a simple text editor - n4+")
print("what you want do?")
print("1 - new file")
print("2 - read file")

def GetTrueInput(nasvay, err):
    usrinputST = input(nasvay)
    while not usrinputST or usrinputST.isspace():
        usrinputST = input(err)
    return usrinputST

def GetMultiLineInput():
    print("\n--- Enter your text (type 'END' on a new line to finish) ---")
    lines = []
    while True:
        line = input()
        if line.strip() == 'END':
            break
        lines.append(line)
    return '\n'.join(lines)

# Выбор имени файла
print("\nFile naming options:")
print("1 - Auto-add .txt extension")
print("2 - Specify full filename with extension (e.g., script.py, data.json)")

file_naming = input("Choose option (1 or 2): ").strip()

if file_naming == "2":
    custom_name = input("Enter filename with extension (e.g., 'script.py', 'notes.txt'): ").strip()
    if custom_name:
        filename = custom_name
    else:
        filename = "untitled.txt"
else:
    custom_name = input("Enter filename (press Enter for 'untitled.txt'): ").strip()
    if custom_name:
        if not custom_name.endswith('.txt'):
            custom_name += '.txt'
        filename = custom_name
    else:
        filename = "untitled.txt"

try:
    print("\nInput mode:")
    print("1 - Single line")
    print("2 - Multiple lines (finish with 'END')")
    input_mode = int(input("Choose mode: "))
except ValueError:
    print("Error: Please enter a number (1 or 2)")
    exit()

try:
    usrcoise = int(input("\nchoice an action: "))
except ValueError:
    print("Error: Please enter a number (1 or 2)")
    exit()

if usrcoise == 1:
    if input_mode == 2:
        usrinputST = GetMultiLineInput()
    else:
        usrinputST = GetTrueInput("_ ", "TypeErr: incorrect format; ")
    
    with open(filename, "w", encoding="utf-8") as file:
        file.write(usrinputST)
    
    print(f"\nV; File '{filename}' saved successfully!")
    
elif usrcoise == 2:
    try:
        with open(filename, "r", encoding="utf-8") as file:
            print(f"\n--- File '{filename}' content ---")
            print(file.read())
    except FileNotFoundError:
        print(f"X; File '{filename}' not found. Create it first (option 1)")
else:
    print("X; Invalid choice")

# в 4:21 утра закончил емае, не дурно