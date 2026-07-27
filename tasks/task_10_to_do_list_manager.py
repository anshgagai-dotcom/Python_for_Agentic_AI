"""Task 10 — To-Do List Manager (menu loop)
Ek khaali list todos = [] banao. Ek while True menu chalao: 1) Add 2) Remove 3) Show 4) Quit. User ke choice ke hisaab se task add/remove/show karo. 4 par loop break karo.

Concepts: while True, match/case (ya if/elif), list .append()/.remove(), break
Hint: remove karte waqt check karo item list mein hai ya nahi (warna crash), if item in todos:."""



todos = []

while True:
    print("\n===== TO-DO MENU =====")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Show Tasks")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter a task: ")
        todos.append(task)
        print("Task added successfully!")
    elif choice == "2":
        task = input("Enter task to remove: ")

        if task in todos:
            todos.remove(task)
            print("Task removed successfully!")
        else:
            print("Task not found!")
    elif choice == "3":

        if len(todos) == 0:
            print("No tasks found.")
        else:
            print("\nYour Tasks:")
            for task in todos:
                print(f"- {task}")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")