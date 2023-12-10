def addlist(tasks, task):
    tasks.append(task)
    print(f'Task "{task}" added.')


def viewlist(tasks):
    print('Tasks:')
    for task in tasks:
        print(f'- {task}')

worklist = []

while True:
    kaj = input('Enter a task (or "exit" to quit): ')
    if kaj.lower() == 'exit':
        break
    addlist(worklist, kaj)

viewlist(worklist)
