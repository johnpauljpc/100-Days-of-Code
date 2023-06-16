print('🌟Life Organizer🌟\n')
print('Welcome to the life organizer. Do you want to add, view, edit or remove a to do?')
tasks = []

def add():
    task = input('What is the task? > ')
    deadline = input('When is it due by? > ')
    priority = input('What is the priority? > ')

    todo = [task, deadline, priority]
    tasks.append(todo)

    print('------ \n Thanks, this task has been added.')
    

    # quit = input('Do you want to see the menu again or quit? > ')

def view():
    for task in tasks:
        for t in task:
            print(t, end='  |  ' )
        print('\n ')


def remove():
    if(len(tasks) == 0):
        print('No task in your todo list!\n')
    
    else:
        task_name = input('what is name of the task you want to remove ?')


        for task in tasks:
            
            if task_name in task[0]: #checks only the task not the due_date nor priority
                tasks.remove(task)
                print(f"\n {task} has been removed \n")
            else:
                print(f'\n {task_name} not found! \n')

            # To View items reamining
            print("****** Available tasks ********")
            for t in task:
                print(t, end='  |  ')
            print('\n')


def edit():
    if(len(tasks) == 0):
        print('No task in your todo list!\n')
    
    else:
        task_name = input('what is name of the task you want to edit ?')


        for task in tasks:
            
            if task_name in task[0]:
                print(f'\n {task} \n')
                print(f"enter the editted version \n")
                tsk = input('task >:  ')
                deadline = input('deadline >:  ')
                priority = input('priority >:  ')
                
                tasks.remove(task)
                task = [tsk, deadline, priority]
                print('\n**** editted *****\n')
                tasks.append(task)

            else:
                print(f'\n {task_name} not found! \n')

            # To View items reamining
            print("****** Available tasks ********")
            for t in task:
                print(t, end='  |  ')
            print('\n')

        


while True:
    action = input('Menu: Add, Remove, View, Edit > ')
    act = action.strip().lower()[0]

    if(act == 'a'):
        add()
    elif(act == 'v'):
        view()
    elif(act == 'r'):
        remove()
    elif(act == 'e'):
        edit()
    else:
        print("\n Bad input, try again \n")
        continue

    quit = input('Do you want to see the menu again or quit? \n To Quit enter quit, while to view Menu enter menu > ')
    if quit.strip().lower()[0] == 'q':
        print(" - - -  Bye - - - ")
        break
    else:
        continue

