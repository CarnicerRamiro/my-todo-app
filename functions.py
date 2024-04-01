import os

FILE_PATH = 'todo.txt'

if not os.path.exists(FILE_PATH):
    with open(FILE_PATH, 'w') as file:
        pass


def get_todos(file_path=FILE_PATH):
    """getter for the todos, you idiot!"""
    with open(file_path, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def set_todos(todos_arg, file_path=FILE_PATH):
    """
    Same as previous but as a setter...
    DUH!
    """
    with open(file_path, 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello from functions")