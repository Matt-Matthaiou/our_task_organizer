from modules.task_list import *
from modules.output import *
from modules.data.task_list import *
from modules.input import *

tasks = []
while(True):
    import_or_not = user_import_or_not()
    if import_or_not.lower() == "y":
        tasks = existing_tasks
        break
    elif import_or_not.lower() == "n":
        break
    else:
        print("Invalid input try Y or N!")


while (True):
    

    print_menu()
    option = main_menu_input()
    if (option.lower() == 'q'):
        break
    if option == '1':
        print_list(tasks)
    elif option == '2':
        print_list(get_uncompleted_tasks(tasks))
    elif option == '3':
        print_list(get_completed_tasks(tasks))
    elif option == '4':
        description = get_description()
        task = get_task_with_description(tasks, description)
        if task is not None:
            mark_task_complete(task)
            print("Task marked complete")
        else:
            print("Task not found")
    elif option == '5':
        time = user_time_input()
        print_list(get_tasks_taking_at_least(tasks, time))
    elif option == '6':
        description = get_task_description()
        print(get_task_with_description(tasks, description))
    elif option == '7':
        description = user_task_description()
        time_taken = user_time_description()
        task = create_task(description, time_taken)
        tasks.append(task)
    else:
        print("Invalid Input - choose another option")

