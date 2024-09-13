to_do_list = []
menu = """
        Select one option
        1.Add Task
        2.Show tasks
        3.Remove task
        4.Exit
       """
    
def addtask():
    task = input("Enter a task : ")
    to_do_list.append(task)
    print(f"{task} has been added to list.")
    
def view_tasks():
    i = 1
    print("List of Tasks : ")
    for task in to_do_list:
        print(f"{i} : {task}")
        i+=1
        
def remove_task():
    view_tasks()
    task_num = int(input("Enter the number of the task to remove: "))
    if 0 < task_num <= len(to_do_list):
        remove = to_do_list.pop(task_num - 1)
        print(f"'{remove}' has been removed from the list.")
    else:
        print("Invalid task number.")   
        
while True:
    print(menu)
    
    ch = int(input("Enter your choice : "))
    
    if ch == 1:
        addtask()
        
    elif ch == 2:
        view_tasks()
        
    elif ch == 3:
        remove_task()
        
    elif ch == 4:
        print("Good Bye...")
        break

    else:
        print("XXXX invalid Choice....")
        print("Please Enter right choice...\U0001F64F\U0001F64F")
         