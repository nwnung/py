class TasksManager:
    try:
        def __init__(self):
            self.tasks = []
        
        def add_task(self,task):
            print(f"se agrego la tarea {task}")
            self.tasks.append(task)
        
        def delete_task(self,task):
            if task in self.tasks:
                print(f"tarea removida {task}")
                self.tasks.remove(task)
            else:
                print(f"tarea no encontrada {task}")

        def show_tasks(self):
            if not self.tasks:
                print("no tienes tareas.")
            else:
                print("tareas actuales:")
                print(f"{self.tasks}")

    except:
        print("something wrong.")
    
chore_one = TasksManager()
chore_one.add_task("make my bed")
chore_one.add_task("take a shower")
chore_one.add_task("make breakfast")

chore_one.show_tasks()
chore_one.delete_task("make my bed")
chore_one.show_tasks()