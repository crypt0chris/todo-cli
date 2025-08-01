def main():
    tasks = []
    while True:
        print("\nOptions: [1] Add  [2] Delete  [3] Show  [4] Quit")
        choice = input("Choose: ")
        if choice == "1":
            task = input("Enter task: ")
            tasks.append(task)
        elif choice == "2":
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            try:
                index = int(input("Delete task #: ")) - 1
                if 0 <= index < len(tasks):
                    tasks.pop(index)
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "3":
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        elif choice == "4":
            print("Bye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
