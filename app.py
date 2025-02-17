todos = []
stop = False


def get_todos():
    global todos
    return todos


def add_one_task(title):
    # your code here
    global todos
    todos.append(title)
    pass


def print_list():
    global todos
    print(todos)


def delete_task(number_to_delete):
    # your code here
    global todos
    myIndex = int(number_to_delete)-1
    del todos[myIndex]
    pass


def save_todos():
    # your code here
    global todos
    f = open('todos.csv', 'w', encoding="utf-8")
    for todo in todos:
        f.write(todo + '\n')
    f.close()


def load_todos():
    # your code here
    global todos
    f = open('todos.csv', 'r', encoding="utf-8")
    linesInTheFile = f.readlines()
    todos.clear()
    for line in linesInTheFile:
        todos.append(line.strip('\n'))
    f.close()


# Below this code will only run if the entry file running was app.py
if __name__ == '__main__':
    while stop == False:
        print("""
    Choose an option: 
        1. Add one task
        2. Delete a task
        3. Print the current list of tasks
        4. Save todo's to todos.csv
        5. Load todo's from todos.csv
        6. Exit
    """)
        response = input()
        if response == "6":
            stop = True
        elif response == "3":
            print_list()
        elif response == "2":
            print("What task number you want to delete?")
            number_to_delete = input()
            delete_task(number_to_delete)
        elif response == "1":
            print("What is your task title?")
            title = input()
            add_one_task(title)
        elif response == "4":
            print("Saving todo's...")
            save_todos()
        elif response == "5":
            print("Loading todo's...")
            load_todos()
        else:
            print("Invalid response, asking again...")
