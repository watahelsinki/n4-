import os

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
    print("|  Navigation: j/k - move line, :n - go to line n, q - quit |")
    print("+" + "-" * 58 + "+")
    print()
    
    lines = []
    current_line = 1
    scroll_offset = 0
    terminal_height = 15
    
    while True:
        clear_screen()
        print_header()
        print("CREATE NEW FILE MODE - MULTILINE INPUT")
        print("=" * 60)
        print()
        
        start_line = scroll_offset + 1
        end_line = min(scroll_offset + terminal_height, len(lines) if lines else 1)
        
        if not lines:
            print("  (empty file)")
            print()
        else:
            for i in range(start_line - 1, end_line):
                if i + 1 == current_line and i < len(lines):
                    print(f"> {i+1:4} | {lines[i]}")
                elif i < len(lines):
                    print(f"  {i+1:4} | {lines[i]}")
                else:
                    print(f"  {i+1:4} | ")
            
            if current_line > len(lines):
                print(f"> {current_line:4} | ")
            elif current_line > end_line:
                for i in range(end_line, current_line - 1):
                    if i < len(lines):
                        print(f"  {i+1:4} | {lines[i]}")
                print(f"> {current_line:4} | ")
        
        print()
        print("-" * 60)
        print(f"Line {current_line}/{len(lines)+1 if lines else 1}")
        print()
        print("Vim-style navigation:")
        print("  j/k - move down/up      |  h/l - page down/up")
        print("  i   - insert text       |  :n  - go to line n")
        print("  x   - delete line       |  e   - edit current line")
        print("  END - finish            |  q   - quit without saving")
        print("-" * 60)
        
        command = input(f"\n[{current_line}] > ").strip()
        
        if command == 'j':
            if current_line <= len(lines):
                current_line += 1
                if current_line > scroll_offset + terminal_height:
                    scroll_offset += 1
            elif current_line == len(lines) + 1:
                print("\n[INFO] Already at end")
                input("Press Enter to continue...")
        elif command == 'k':
            if current_line > 1:
                current_line -= 1
                if current_line <= scroll_offset:
                    scroll_offset -= 1
            else:
                print("\n[INFO] Already at top")
                input("Press Enter to continue...")
        elif command == 'h':
            if scroll_offset + terminal_height < len(lines) + 1:
                scroll_offset += terminal_height
                current_line = min(scroll_offset + 1, len(lines) + 1)
            else:
                print("\n[INFO] Already at bottom")
                input("Press Enter to continue...")
        elif command == 'l':
            if scroll_offset > 0:
                scroll_offset = max(0, scroll_offset - terminal_height)
                current_line = scroll_offset + 1
            else:
                print("\n[INFO] Already at top")
                input("Press Enter to continue...")
        elif command == 'i':
            if current_line <= len(lines):
                line_text = lines[current_line - 1]
                print(f"\nEditing line {current_line}:")
                new_text = input(f"[{current_line}] > {line_text}\nNew text: ")
                if new_text:
                    lines[current_line - 1] = new_text
                else:
                    lines[current_line - 1] = line_text
            else:
                print(f"\nAdding new line {current_line}:")
                new_text = input(f"[{current_line}] > ")
                if new_text:
                    lines.insert(current_line - 1, new_text)
        elif command == 'e':
            if current_line <= len(lines):
                line_text = lines[current_line - 1]
                print(f"\nEditing line {current_line}:")
                print(f"Current: {line_text}")
                new_text = input("New text: ")
                if new_text:
                    lines[current_line - 1] = new_text
            else:
                print(f"\n[INFO] Line {current_line} is empty, use 'i' to add text")
                input("Press Enter to continue...")
        elif command == 'x':
            if current_line <= len(lines) and len(lines) > 0:
                deleted = lines.pop(current_line - 1)
                print(f"\n[INFO] Deleted line {current_line}: {deleted}")
                if current_line > len(lines) and current_line > 1:
                    current_line -= 1
                if scroll_offset > len(lines) - terminal_height:
                    scroll_offset = max(0, len(lines) - terminal_height)
                input("Press Enter to continue...")
            else:
                print("\n[INFO] No line to delete")
                input("Press Enter to continue...")
        elif command.startswith(':'):
            try:
                line_num = int(command[1:])
                if 1 <= line_num <= len(lines) + 1:
                    current_line = line_num
                    scroll_offset = max(0, min(line_num - 1, len(lines) + 1 - terminal_height))
                else:
                    print(f"\n[ERROR] Line number must be between 1 and {len(lines) + 1}")
                    input("Press Enter to continue...")
            except ValueError:
                print("\n[ERROR] Invalid line number")
                input("Press Enter to continue...")
        elif command == 'END':
            break
        elif command == 'q':
            print("\n[INFO] Exiting without saving")
            return None
        else:
            print("\n[ERROR] Unknown command")
            input("Press Enter to continue...")
    
    return '\n'.join(lines)

def display_with_navigation(content, filename):
    lines = content.splitlines()
    total_lines = len(lines)
    current_line = 1
    scroll_offset = 0
    terminal_height = 20
    
    while True:
        clear_screen()
        print_header()
        print(f"READING: {filename}  [{current_line}/{total_lines}]")
        print("=" * 60)
        print()
        
        start_line = scroll_offset + 1
        end_line = min(scroll_offset + terminal_height, total_lines)
        
        for i in range(start_line - 1, end_line):
            if i + 1 == current_line:
                print(f"> {i+1:4} | {lines[i]}")
            else:
                print(f"  {i+1:4} | {lines[i]}")
        
        print()
        print("-" * 60)
        print("Vim-style navigation:")
        print("  j/k - move down/up       |  Ctrl+d/u - half page down/up")
        print("  h/l - page down/up       |  gg/G    - go to top/bottom")
        print("  :n   - go to line n      |  /text   - search")
        print("  q    - quit")
        print("-" * 60)
        
        command = input("\n> ").strip()
        
        if command == 'j':
            if current_line < total_lines:
                current_line += 1
                if current_line > scroll_offset + terminal_height:
                    scroll_offset += 1
        elif command == 'k':
            if current_line > 1:
                current_line -= 1
                if current_line <= scroll_offset:
                    scroll_offset -= 1
        elif command == 'h':
            if scroll_offset + terminal_height < total_lines:
                scroll_offset += terminal_height
                current_line = min(scroll_offset + 1, total_lines)
            else:
                print("\n[INFO] Already at bottom")
                input("Press Enter to continue...")
        elif command == 'l':
            if scroll_offset > 0:
                scroll_offset = max(0, scroll_offset - terminal_height)
                current_line = scroll_offset + 1
            else:
                print("\n[INFO] Already at top")
                input("Press Enter to continue...")
        elif command == 'gg':
            current_line = 1
            scroll_offset = 0
        elif command == 'G':
            current_line = total_lines
            scroll_offset = max(0, total_lines - terminal_height)
        elif command == 'ctrl+d':
            half_page = terminal_height // 2
            if current_line + half_page <= total_lines:
                current_line += half_page
                if current_line > scroll_offset + terminal_height:
                    scroll_offset = min(scroll_offset + half_page, total_lines - terminal_height)
            else:
                current_line = total_lines
                scroll_offset = max(0, total_lines - terminal_height)
        elif command == 'ctrl+u':
            half_page = terminal_height // 2
            if current_line - half_page >= 1:
                current_line -= half_page
                if current_line <= scroll_offset:
                    scroll_offset = max(0, scroll_offset - half_page)
            else:
                current_line = 1
                scroll_offset = 0
        elif command.startswith(':'):
            try:
                line_num = int(command[1:])
                if 1 <= line_num <= total_lines:
                    current_line = line_num
                    scroll_offset = max(0, min(line_num - 1, total_lines - terminal_height))
                else:
                    print(f"\n[ERROR] Line number must be between 1 and {total_lines}")
                    input("Press Enter to continue...")
            except ValueError:
                print("\n[ERROR] Invalid line number")
                input("Press Enter to continue...")
        elif command.startswith('/'):
            search_term = command[1:]
            if search_term:
                found = False
                for i in range(current_line, total_lines + 1):
                    if search_term.lower() in lines[i-1].lower():
                        current_line = i
                        scroll_offset = max(0, min(i - 1, total_lines - terminal_height))
                        print(f"\n[FOUND] '{search_term}' at line {i}")
                        found = True
                        break
                if not found:
                    for i in range(1, current_line):
                        if search_term.lower() in lines[i-1].lower():
                            current_line = i
                            scroll_offset = max(0, min(i - 1, total_lines - terminal_height))
                            print(f"\n[FOUND] '{search_term}' at line {i}")
                            found = True
                            break
                if not found:
                    print(f"\n[INFO] '{search_term}' not found")
                    input("Press Enter to continue...")
            else:
                print("\n[ERROR] Search term cannot be empty")
                input("Press Enter to continue...")
        elif command == 'q':
            break
        else:
            print("\n[ERROR] Unknown command")
            input("Press Enter to continue...")

def create_file():
    print_header()
    print("CREATE NEW FILE MODE")
    print()
    
    print("+--------------------------------------------------------+")
    print("|  Input Mode                                           |")
    print("|  1 - Single line                                      |")
    print("|  2 - Multiple lines with navigation                   |")
    print("+--------------------------------------------------------+")
    
    try:
        input_mode = int(input("\n> Choose mode (1/2): "))
        if input_mode not in [1, 2]:
            print("\n[ERROR] Please enter 1 or 2")
            return
    except ValueError:
        print("\n[ERROR] Please enter a number (1 or 2)")
        return
    
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
    
    print()
    if input_mode == 2:
        content = GetMultiLineInput()
        if content is None:
            return
    else:
        content = GetTrueInput("> Enter text: ", "[ERROR] Incorrect format; try again: ")
    
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
    
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
        
        if not content:
            print()
            print("+" + "-" * 58 + "+")
            print("|  FILE IS EMPTY                                      |")
            print("+" + "-" * 58 + "+")
            print(f"\nFile: {filename} is empty (0 characters)")
            input("\n\nPress Enter to continue...")
            return
        
        display_with_navigation(content, filename)
        
    except FileNotFoundError:
        print(f"\n[ERROR] File '{filename}' not found. Create it first (option 1)")
        input("\nPress Enter to continue...")
    except Exception as e:
        print(f"\n[ERROR] Error reading file: {e}")
        input("\nPress Enter to continue...")

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
#bullshit