
FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """  This function opens a file and returns a list of the file to-do contents
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()

        return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """   This function opens a file and writes a list into the file, and then closes and save the file

    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__" :
    print("Hello")
    print(get_todos())