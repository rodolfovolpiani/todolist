import json


def load_tasks():
    try:
        with open('data.json', 'r') as file:
            tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []
    return tasks


def save_tasks(tasks):
    with open('data.json', 'w') as file:
        json.dump(tasks, file)


def list_tasks():
    tasks = load_tasks()
    if tasks:
        print("Lista de Tarefas:")
        for index, task in enumerate(tasks, start=1):
            status = "Concluída" if task['done'] else "Pendente"
            print(f"{index}. {task['title']} - {status}")
    else:
        print("Nenhuma tarefa encontrada.")


def add_task(title):
    tasks = load_tasks()
    tasks.append({'title': title, 'done': False})
    save_tasks(tasks)
    print(f"Tarefa '{title}' adicionada.")


def complete_task(task_index):
    tasks = load_tasks()
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1]['done'] = True
        save_tasks(tasks)
        print(f"Tarefa '{tasks[task_index - 1]['title']}' marcada como concluída.")
    else:
        print("Índice de tarefa inválido.")



