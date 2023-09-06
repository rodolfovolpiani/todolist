import tasks  # Importa o módulo tasks.py

if __name__ == '__main__':
    while True:
        print("\n===== Lista de Tarefas CLI =====")
        print("1. Listar Tarefas")
        print("2. Adicionar Tarefa")
        print("3. Marcar Tarefa como Concluída")
        print("4. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            tasks.list_tasks()  # Chama a função list_tasks() do módulo tasks.py
        elif choice == '2':
            title = input("Digite o título da nova tarefa: ")
            tasks.add_task(title)  # Chama a função add_task() do módulo tasks.py
        elif choice == '3':
            tasks.list_tasks()
            task_index = int(input("Digite o número da tarefa a ser marcada como concluída: "))
            tasks.complete_task(task_index)  # Chama a função complete_task() do módulo tasks.py
        elif choice == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Escolha novamente.")
