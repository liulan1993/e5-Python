import os

def display_menu():
    print("************ 简易记事本 ************")
    print("1. 查看记事本内容")
    print("2. 添加新的记录")
    print("3. 删除记录")
    print("4. 退出程序")
    print("***********************************")

def view_notes():
    with open("notes.txt", "r") as file:
        notes = file.read()
        print("记事本内容：")
        print(notes)

def add_note():
    note = input("请输入新的记录：")
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    print("记录已添加。")

def delete_note():
    view_notes()
    index = int(input("请输入要删除的记录索引：")) - 1
    with open("notes.txt", "r") as file:
        notes = file.readlines()
    if index >= 0 and index < len(notes):
        del notes[index]
        with open("notes.txt", "w") as file:
            file.writelines(notes)
        print("记录已删除。")
    else:
        print("无效的索引。")

def main():
    while True:
        display_menu()
        choice = input("请输入选项：")
        if choice == "1":
            view_notes()
        elif choice == "2":
            add_note()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            print("感谢使用记事本。再见！")
            break
        else:
            print("无效的选项。")

if __name__ == "__main__":
    if not os.path.exists("notes.txt"):
        with open("notes.txt", "w") as file:
            pass
    main()
