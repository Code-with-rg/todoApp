
print("Welcome to the To-Do List App!")
while True:
    userInput = input('What do u want  to do ? (add/view/update/delete/exit): ').strip().lower()
    if userInput.lower().strip() == 'exit':
        break

    match userInput:
        case 'add':
            userTime = input("Enter your time: ")
            userTask = input("Enter your task: ")
            with open('todo.txt', 'a') as f:
                f.write(f"{userTime} --> {userTask}\n")
            print("Task added successfully.")
        case 'view':
            userTask = input("Enter the task you want to view: ")
            with open('todo.txt', 'r') as f:
                if userTask == "all":
                    tasks = f.read()
                    print("All tasks:")
                    print(tasks)
                    continue
                tasks = f.readlines()
                if not tasks:
                    print("No tasks found.")
                    continue
                for task in tasks:
                    if userTask in task:
                        print(task.strip())
            continue
        case 'update':
            userTask = input("Enter the task you want to update: ")
            with open('todo.txt', 'r') as f:
                tasks = f.readlines()
            with open('todo.txt', 'w') as f:
                for task in tasks:
                    if userTask in task:
                        userTime = input("Enter updated time: ")
                        newTask = input("Enter the updated task: ")
                        f.write(f"{userTime} --> {newTask}\n")
                    else:
                        f.write(task)
            continue
        case 'delete':
            userTask = input("Enter the task you want to delete: ")
            with open('todo.txt', 'r') as f:
                tasks = f.readlines()
            with open('todo.txt', 'w') as f:
                for task in tasks:
                    if userTask not in task:
                        f.write(task)
                        print(f"Task '{userTask}' not found.")
                        continue
            print("Task deleted successfully.")
        case _:
            print("Invalid option. Please try again.")
            
