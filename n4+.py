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


# ================= MULTILINE EDITOR ================= #

def GetMultiLineInput():
    lines = []
    current_line = 1
    scroll_offset = 0
    terminal_height = 15

    # ---------- COMMANDS ---------- #

    def cmd_write(ctx):
        print("\n[INFO] Saved")
        return 'SAVE'

    def cmd_quit(ctx):
        print("\n[INFO] Exit without saving")
        return 'QUIT'

    def cmd_wq(ctx):
        print("\n[INFO] Saved and exited")
        return 'SAVE_QUIT'

    def cmd_delete(ctx):
        lines = ctx["lines"]
        cl = ctx["current_line"]

        if 1 <= cl <= len(lines):
            deleted = lines.pop(cl - 1)
            print(f"\n[INFO] Deleted: {deleted}")
            if ctx["current_line"] > len(lines):
                ctx["current_line"] = max(1, len(lines))
        else:
            print("\n[INFO] Nothing to delete")
        input("Press Enter...")

    commands = {
        "w": cmd_write,
        "q": cmd_quit,
        "wq": cmd_wq,
        "d": cmd_delete,
    }

    # ---------- LOOP ---------- #

    while True:
        clear_screen()
        print_header()
        print("MULTILINE EDITOR")
        print("=" * 60)

        # отображение
        if not lines:
            print("(empty)")
        else:
            for i in range(scroll_offset, min(len(lines), scroll_offset + terminal_height)):
                marker = ">" if i + 1 == current_line else " "
                print(f"{marker} {i+1:4} | {lines[i]}")

        print("\nCommands:")
        print(" j/k - move   | i - insert/edit")
        print(" x   - delete | :cmd - command mode")
        print(" END - save   | q - quit")
        print("-" * 60)

        command = input(f"\n[{current_line}] > ").strip()

        # ---------- NAVIGATION ----------
        if command == 'j':
            if current_line < len(lines) + 1:
                current_line += 1

        elif command == 'k':
            if current_line > 1:
                current_line -= 1

        # ---------- INSERT ----------
        elif command == 'i':
            text = input("Insert: ")
            if current_line <= len(lines):
                lines[current_line - 1] = text
            else:
                lines.append(text)

        # ---------- DELETE ----------
        elif command == 'x':
            if 1 <= current_line <= len(lines):
                lines.pop(current_line - 1)

        # ---------- COMMAND MODE ----------
        elif command.startswith(':'):
            ctx = {
                "lines": lines,
                "current_line": current_line,
                "scroll_offset": scroll_offset
            }

            cmds = command[1:].split('|')

            for raw in cmds:
                cmd = raw.strip()

                # переход к строке
                if cmd.isdigit():
                    num = int(cmd)
                    if 1 <= num <= len(lines) + 1:
                        current_line = num
                        ctx["current_line"] = num
                    continue

                parts = cmd.split()
                name = parts[0]
                args = parts[1:]

                if name in commands:
                    result = commands[name](ctx)

                    current_line = ctx["current_line"]

                    if result == 'QUIT':
                        return None
                    elif result == 'SAVE':
                        return '\n'.join(lines)
                    elif result == 'SAVE_QUIT':
                        return '\n'.join(lines)
                else:
                    print(f"\n[ERROR] Unknown command: {cmd}")
                    input("Press Enter...")

        # ---------- EXIT ----------
        elif command == 'END':
            return '\n'.join(lines)

        elif command == 'q':
            return None

        else:
            print("\n[ERROR] Unknown command")
            input("Press Enter...")


# ================= FILE VIEWER ================= #

def display_with_navigation(content, filename):
    lines = content.splitlines()
    current_line = 1

    while True:
        clear_screen()
        print_header()
        print(f"READING: {filename}")
        print("=" * 60)

        for i, line in enumerate(lines):
            marker = ">" if i + 1 == current_line else " "
            print(f"{marker} {i+1:4} | {line}")

        print("\nCommands: j/k, q")
        cmd = input("> ").strip()

        if cmd == 'j' and current_line < len(lines):
            current_line += 1
        elif cmd == 'k' and current_line > 1:
            current_line -= 1
        elif cmd == 'q':
            break


# ================= CREATE FILE ================= #

def create_file():
    print_header()
    print("CREATE FILE")

    mode = input("1-single line, 2-multiline: ").strip()

    filename = input("Filename: ").strip()
    if not filename:
        filename = "untitled.txt"
    if '.' not in filename:
        filename += ".txt"

    if mode == '2':
        content = GetMultiLineInput()
        if content is None:
            return
    else:
        content = GetTrueInput("> ", "Retry: ")

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"\nSaved: {filename}")
    input("Enter...")


# ================= READ FILE ================= #

def read_file():
    print_header()
    filename = input("Filename: ").strip()

    if '.' not in filename:
        filename += ".txt"

    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()

        display_with_navigation(content, filename)

    except:
        print("File not found")
        input("Enter...")


# ================= MAIN ================= #

def main():
    while True:
        print_header()
        print("1 - Create")
        print("2 - Read")
        print("3 - Exit")

        choice = input("> ").strip()

        if choice == '1':
            create_file()
        elif choice == '2':
            read_file()
        elif choice == '3':
            break


if __name__ == "__main__":
    main()
#watafak, i hate ts shit