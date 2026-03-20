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

# Выбор имени файла
custom_name = input("Enter filename (press Enter for 'untitled.txt'): ").strip()
if custom_name:
    if not custom_name.endswith('.txt'):
        custom_name += '.txt'
    filename = custom_name
else:
    filename = "untitled.txt"

try:
    usrcoise = int(input("choice an action: "))
except ValueError:
    print("Error: Please enter a number (1 or 2)")
    exit()

if usrcoise == 1:
    usrinputST = GetTrueInput("_ ", "TypeErr: incorrect format; ")
    
    with open(filename, "w", encoding="utf-8") as file:
        file.write(usrinputST)
    
    print(f"V; File '{filename}' saved successfully!")
    
elif usrcoise == 2:
    try:
        with open(filename, "r", encoding="utf-8") as file:
            print(f"\n--- File '{filename}' content ---")
            print(file.read())
    except FileNotFoundError:
        print(f"X; File '{filename}' not found. Create it first (option 1)")
else:
    print("X; Invalid choice")


    #в 4:21 утра закончил емае, не дурно
    
    