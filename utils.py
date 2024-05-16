FILEPATH = "todos.txt"


def get_todos(path=FILEPATH):
    with open(path, "r") as file:
        todos = file.readlines()
    return todos


def set_todos(todos, path=FILEPATH):
    with open(path, "w") as file:
        file.writelines(todos)


def store_removed_todo(removed):
    current_removed = get_removed_todos()
    current_removed.append(removed)
    with open("removed_todos.txt", "w") as file:
        file.writelines(current_removed)


def get_removed_todos():
    with open("removed_todos.txt", 'r') as file:
        removed_todos = file.readlines()
    return removed_todos
