class Todo:

    def __init__(self):
        self.todos = []

    def add(self, todo):
        self.todos.append(todo)
    
    def view(self):
        print("Todo List:")
        for i, todo in enumerate(self.todos, start=1):
            print(f"{i}. {todo}")

    def delete(self, index):
         #using the index to delete
         if 0 < index <= len(self.todos):
            deleted_todo = self.todos.pop(index - 1)
            print(f"Todo '{deleted_todo}' deleted.")
         else:
            print("Invalid todo number.")

todoList = Todo()

while True:
    print("todo menu: \n")
    print("1. add todo ")
    print("2. view todo list")
    print("3. delete todo")

    choice = input("enter your choice: ")

    if choice == '1':
        todo = input("Enter the todo description: ")
        todoList.add(todo)
    elif choice == '2':
        todoList.view()

    elif choice == '3':
        todoList.view()
        try:
            todoId = int(input("Enter the todo number to delete: "))
            todoList.delete(todoId)
        except ValueError:
                print("Invalid id. Please enter a number.")
        # todoList.delete()


    else:
        print("invalid choice")
