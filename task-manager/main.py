class Task():
    def __init__(self,name,description) -> None:
        self.name = name
        self.description = description

    def __str__(self) -> str:
        return f'Name: {self.name} - Description: {self.description} - Completed?: {self.completed}'

class TaskGenerator():
    def __init__(self) -> None:
        self.tasks = []

    def show_tasks(self):
        if len(self.tasks) > 0:
            print('Your tasks: ')
            for i, task in enumerate(self.tasks,start=1):
                print(f'{i}. - {task.name} - {task.description}')
        else:
            print('No tasks yet')

    def add_task(self):
        name = input('Name of task: ')
        description = input('Description of task: ')

        new_task = Task(name,description)

        self.tasks.append(new_task)
        print(self.tasks)

    def delete_task(self):
        self.show_tasks()
        try:
            selected_task = int(input('Number of deleted task: ')) - 1

            if 0 >= selected_task > len(self.tasks):
                removed_task = self.tasks.pop(selected_task)
                print(f'Task "{removed_task.name}" deleted sucesfully!')
            else:
                print('Invalid task number')
            

        except ValueError:
            print('Something wrong. Please enter a valid number')

    def init(self):
        while True:
            print("\n WELCOME TASK MANAGER \n")
            print("1. ADD TASK")
            print("2. DELETE TASK")
            print("3. SHOW TASKS")
            print("4. EXIT")
            

            option = input('SELECT NUMBER OPTION: ')

            if option == '1':
                self.add_task()
            elif option == '2':
                self.delete_task()
            elif option  == '3':
                self.show_tasks()
            elif option == '4':
                print('Exiting...')
                break
            else:
                print('Please select a number between 1 and 4.')


if __name__ == '__main__':
    task_manager = TaskGenerator()
    task_manager.init()