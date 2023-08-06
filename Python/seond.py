# define a list to store tasks
tasks = []

# define a function to add tasks to the list
def add_task(task):
    tasks.append(task)

# define a function to remove tasks from the list
def remove_task(task):
    tasks.remove(task)

# define a function to display the tasks in the list
def show_tasks():
    for task in tasks:
        print(task)

# add a loop to keep the chatbot running
while True:
    user_input = input('What would you like to do? ')
    if user_input == 'add':
        task = input('Enter the task to add: ')
        add_task(task)
    elif user_input == 'remove':
        task = input('Enter the task to remove: ')
        remove_task(task)
    elif user_input == 'show':
        show_tasks()
    elif user_input == 'quit':
        break
    else:
        print('Invalid input!')