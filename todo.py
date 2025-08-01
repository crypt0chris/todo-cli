import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return [line.strip() for line in f.readlines()]
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        f.writelines(f"{task}\n" for task in tasks)

def main():
    tasks = load_tasks()
    while True:
        print("\nOptions: [1] Add  [2] Delete  [3] Show  [4] Quit")
        choice = input("Choose an option (1-4): ").strip()
        if choice == "1":
            task = input("Enter a new task: ").strip()
            if task:
                print("Set priority: [1] 🔴 High  [2] 🟡 Medium  [3] 🟢 Low")
                p_choice = input("Choose priority (1-3): ").strip()
                if p_choice == "1":
                    priority = "🔴"
                elif p_choice == "2":
                    priority = "🟡"
                elif p_choice == "3":
                    priority = "🟢"
                else:
                    priority = "⚪️"  # default if invalid
                task = f"[{priority}] {task}"
                tasks.append(task)
                save_tasks(tasks)
                print("✅ Task added.")
            else:
                print("⚠️ Task cannot be empty.")
        elif choice == "2":
            if not tasks:
                print("⚠️ No tasks to delete.")
                continue
            print("\nYour tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            try:
                index = int(input("Enter task number to delete: ")) - 1
                if 0 <= index < len(tasks):
                    removed = tasks.pop(index)
                    save_tasks(tasks)
                    print(f"🗑 Removed: {removed}")
                else:
                    print("❌ Invalid task number.")
            except ValueError:
                print("❌ Please enter a valid number.")
        elif choice == "3":
            if not tasks:
                print("📭 No tasks to show.")
            else:
                print("\nYour tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option. Please choose 1-4.")

if __name__ == "__main__":
    main()
