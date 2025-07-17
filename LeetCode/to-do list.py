import sys
print(sys.path)

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        print("Remember, dear User, you always can left just write a command 'exit'.")
        while True:
            new_task = str(input("Enter a new task: "))
            if new_task.lower() == "exit":
                break
            self.tasks.append(new_task)
        print(f"You successfully added task: {self.tasks}")

    def remove_task(self):
        while True:
            question = str(input("What task would you like to delete? \nor you can just exit enter 'exit': "))
            if question.lower() == "exit":
                break
            elif any(question) in self.tasks:
                self.tasks.remove(question)
            else:
                print("There is no such task.")

    def show_tasks(self):
        print(self.tasks)

todo = ToDoList()

todo.add_task()
todo.remove_task()
todo.show_tasks()