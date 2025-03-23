# todo.py
tasks = []

def add_task(task):
    tasks.append(task)
    print(f'Task "{task}" added.')

def list_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for idx, task in enumerate(tasks, start=1):
            print(f'{idx}. {task}')

def complete_task(task_idx):
    if 0 < task_idx <= len(tasks):
        tasks[task_idx - 1] += " (Completed)"
        print(f'Task {task_idx} marked as completed.')
    else:
        print("Invalid task index.")

if __name__ == "__main__":
    add_task("Finish Assignment")
    list_tasks()
