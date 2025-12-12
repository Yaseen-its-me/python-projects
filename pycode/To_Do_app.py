#!/usr/bin/python3

import time
 
t = time.localtime(time.time())
localtime = time.asctime(t)
str = "Current Time:" + time.asctime(t)
 
print(str)
class To_Do_App:
    def __init__(self):
        self.tasks=[]
    def add_task(self):
        task=input('Enter your task: ')    
        self.tasks.append(task)
        print(f" Task {task} added successfully ! ")
    def remove_task(self)  :
        task=input('Enter which task is to be removed: ') 
        if task in self.tasks:
            self.tasks.remove(task) 
            print(f" Task {task} is removed successfully ! ")
        else:
            print(f" Task{task} is not found")    
    def view_tasks(self):
        if not self.tasks:
            print('No tasks available')   
        else :
            print('Available tasks')   
            for i, task in enumerate(self.tasks,start=1):
                print(f"{i}. {task}")     
    def mark_task_complete(self):
        task=input('Enter a task to mark it : ') 
        if task in self.tasks:
            self.tasks.remove(task) 
            print(f" Task {task} is  completely marked ! ")
        else:
            print(f" Task{task} is not found")    
def main() :
    app=To_Do_App()   
    is_running=True
    while is_running:
        print("-----------\n. To_Do App Menu\n-------------")    
        print("1.Add task\n2.remove task\n3.view tasks\n4.mark\n5.Exit")   
        choice=input('Enter your choice(1-5): ')
        if choice=="1":
            app.add_task()
        elif choice=="2":
                app.remove_task()
        elif choice=="3":
                app.view_tasks()
        elif choice=="4" :
                app.mark_task_complete() 
        elif choice=="5"   :
                print("Exiting  the app") 
                is_running=False
        else:
            print("Invalid choice. please try again")   
    print("Thank you")        
if __name__=="__main__" :
    main()
                  
                   
            
                   