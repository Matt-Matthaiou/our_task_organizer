

# Functions to complete:

## Get a list of uncompleted tasks
def get_uncompleted_tasks(list):
    uncompleted_tasks =[]
    for task in list:
        if task["completed"] == False:
            uncompleted_tasks.append(task)
    return uncompleted_tasks
    
    

## Get a list of completed tasks
def get_completed_tasks(list):
    completed_tasks =[]
    for task in list:
        if task["completed"]:
            completed_tasks.append(task)
    return completed_tasks

## Get tasks where time_taken is at least a given time
def get_tasks_taking_at_least(list, time):
    fitting_tasks=[]
    for task in list:
        if task["time_taken"] >= int(time):
            fitting_tasks.append(task)
    return fitting_tasks
## Find a task with a given description
def get_task_with_description(list, description):
    fitting_tasks=[]
    for task in list:
        if task["description"] == str(description):
            fitting_tasks.append(task)
    return fitting_tasks

# Extention (Function): 

## Get a list of tasks by status
def get_tasks_by_status(list, status):
    if status == True:
        completed_tasks= []
        for task in tasks:
            if task["completed"] == True:
                completed_tasks.append(task)
        return completed_tasks
    elif status == False:
        uncompleted_tasks= []
        for task in tasks:
            if task["completed"] == False:
                uncompleted_tasks.append(task)
        return uncompleted_tasks 
    else:
        return "That is not a valid status"
    


        


def mark_task_complete(task):
    task[0]["completed"] = True

def create_task(description, time_taken):
    task = {}
    task["description"] = description
    task["completed"] = False
    task["time_taken"] = time_taken

    return task

def add_to_list(list, task):
    list.append(task)



