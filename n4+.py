import os

# ASCII Art
LOGO = r"""
+---------------------------------+
|                  .o             |
|                .d88             |
|ooo. .oo.     .d'888       88    |
|`888P"Y88b  .d'  888       88    |
| 888   888  88ooo888oo 8888888888|
| 888   888       888       88    |
|o888o o888o     o888o      88    |
+---------------------------------+

                                                                               
"""

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    clear_screen()
    print(LOGO)
    print("=" * 60)
    print()

def GetTrueInput(prompt, error_msg):
    user_input = input(prompt)
    while not user_input or user_input.isspace():
        user_input = input(error_msg)
    return user_input

def GetMultiLineInput():
    print()
    print("+" + "-" * 58 + "+")
    print("|  Enter your text (type 'END' on a new line to finish)  |")
    print("+" + "-" * 58 + "+")
    print()
    lines = []
    line_count = 1
    while True:
        try:
            line = input(f"{line_count:3} | ")
            if line.strip() == 'END':
                break
            lines.append(line)
            line_count += 1
        except KeyboardInterrupt:
            print("\n\nInput cancelled by user")
            return None
    return '\n'.join(lines)

def create_file():
    print_header()
    print("CREATE NEW FILE MODE")
    print()
    
    # Input mode selection
    print("+--------------------------------------------------------+")
    print("|  Input Mode                                           |")
    print("|  1 - Single line                                      |")
    print("|  2 - Multiple lines (finish with 'END')               |")
    print("+--------------------------------------------------------+")
    
    try:
        input_mode = int(input("\n> Choose mode (1/2): "))
        if input_mode not in [1, 2]:
            print("\n[ERROR] Please enter 1 or 2")
            return
    except ValueError:
        print("\n[ERROR] Please enter a number (1 or 2)")
        return
    
    # File naming selection
    print()
    print("+--------------------------------------------------------+")
    print("|  File Naming                                          |")
    print("|  1 - Auto-add .txt extension                          |")
    print("|  2 - Specify full filename with extension             |")
    print("|      (e.g., script.py, data.json, notes.txt)          |")
    print("+--------------------------------------------------------+")
    
    file_naming = input("\n> Choose option (1/2): ").strip()
    
    if file_naming == "2":
        custom_name = input("\n> Enter filename with extension: ").strip()
        if custom_name:
            filename = custom_name
        else:
            filename = "untitled.txt"
            print("   [INFO] Using default: untitled.txt")
    else:
        custom_name = input("\n> Enter filename (press Enter for 'untitled.txt'): ").strip()
        if custom_name:
            if not custom_name.endswith('.txt'):
                custom_name += '.txt'
            filename = custom_name
        else:
            filename = "untitled.txt"
    
    # Content input
    print()
    if input_mode == 2:
        content = GetMultiLineInput()
        if content is None:
            return
    else:
        content = GetTrueInput("> Enter text: ", "[ERROR] Incorrect format; try again: ")
    
    # Save file
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)
        
        print()
        print("+" + "-" * 58 + "+")
        print("|  [SUCCESS] FILE SAVED SUCCESSFULLY!                 |")
        print("+" + "-" * 58 + "+")
        print(f"\nFile: {filename}")
        print(f"Size: {len(content)} characters")
        print(f"Lines: {len(content.splitlines())}")
        
    except Exception as e:
        print(f"\n[ERROR] Error saving file: {e}")
    
    input("\n\nPress Enter to continue...")

def read_file():
    print_header()
    print("READ FILE MODE")
    print()
    
    # File naming selection
    print("+--------------------------------------------------------+")
    print("|  File Naming                                          |")
    print("|  1 - Auto-add .txt extension                          |")
    print("|  2 - Specify full filename with extension             |")
    print("|      (e.g., script.py, data.json, notes.txt)          |")
    print("+--------------------------------------------------------+")
    
    file_naming = input("\n> Choose option (1/2): ").strip()
    
    if file_naming == "2":
        custom_name = input("\n> Enter filename with extension: ").strip()
        if custom_name:
            filename = custom_name
        else:
            print("\n[ERROR] Filename cannot be empty")
            input("\nPress Enter to continue...")
            return
    else:
        custom_name = input("\n> Enter filename (press Enter for 'untitled.txt'): ").strip()
        if custom_name:
            if not custom_name.endswith('.txt'):
                custom_name += '.txt'
            filename = custom_name
        else:
            filename = "untitled.txt"
    
    # Read file
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
        
        print()
        print("+" + "-" * 58 + "+")
        print(f"|  FILE CONTENT: {filename:<40} |")
        print("+" + "-" * 58 + "+")
        print()
        print(content)
        print()
        print("+" + "-" * 58 + "+")
        print(f"|  Size: {len(content)} characters | Lines: {len(content.splitlines())}                  |")
        print("+" + "-" * 58 + "+")
        
    except FileNotFoundError:
        print(f"\n[ERROR] File '{filename}' not found. Create it first (option 1)")
    except Exception as e:
        print(f"\n[ERROR] Error reading file: {e}")
    
    input("\n\nPress Enter to continue...")

def main():
    while True:
        print_header()
        print("MAIN MENU")
        print()
        print("+--------------------------------------------------------+")
        print("|  1 - Create new file                                   |")
        print("|  2 - Read existing file                                |")
        print("|  3 - Exit                                              |")
        print("+--------------------------------------------------------+")
        
        try:
            choice = int(input("\n> Choose action (1/2/3): "))
        except ValueError:
            print("\n[ERROR] Please enter a number (1, 2, or 3)")
            input("\nPress Enter to continue...")
            continue
        
        if choice == 1:
            create_file()
        elif choice == 2:
            read_file()
        elif choice == 3:
            print_header()
            print("Goodbye!")
            print()
            print("+--------------------------------------------------------+")
            print("|  Thank you for using TextEditor by n4+                 |")
            print("+--------------------------------------------------------+")
            break
        else:
            print("\n[ERROR] Invalid choice. Please enter 1, 2, or 3")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()

#я прям устал уже епт
#зачем я это пишу если есть vim?