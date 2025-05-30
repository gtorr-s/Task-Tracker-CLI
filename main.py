import argparse
import json
import os
from datetime import datetime

# Caminho do arquivo JSON onde as tarefas serão salvas
tasks_file = 'tasks.json'

# Carrega as tarefas do arquivo JSON, retorna lista de tarefas
def load_tasks():
    # Se o arquivo não existir, cria um JSON vazio
    if not os.path.exists(tasks_file):
        with open(tasks_file, 'w', encoding='utf-8') as f:
            json.dump([], f, ensure_ascii=False, indent=4)
        return []
    try:
        with open(tasks_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        print('Erro ao ler o arquivo de tarefas. Verifique o JSON.')
        return []

# Salva a lista de tarefas no arquivo JSON
def save_tasks(tasks):
    with open(tasks_file, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, ensure_ascii=False, indent=4)

# Gera o próximo ID único
def get_next_id(tasks):
    if not tasks:
        return 1
    return max(task['id'] for task in tasks) + 1

# Adiciona uma nova tarefa
def add_task(description):
    tasks = load_tasks()
    new_id = get_next_id(tasks)
    now = datetime.now().isoformat()
    task = {
        'id': new_id,
        'description': description,
        'status': 'todo',
        'createdAt': now,
        'updatedAt': now
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f'Tarefa adicionada com sucesso (ID: {new_id})')

# Atualiza a descrição de uma tarefa existente
def update_task(task_id, new_desc):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = new_desc
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print('Tarefa atualizada com sucesso.')
            return
    print('Tarefa não encontrada.')

# Deleta uma tarefa pelo ID
def delete_task(task_id):
    tasks = load_tasks()
    tasks_filtered = [t for t in tasks if t['id'] != task_id]
    if len(tasks_filtered) == len(tasks):
        print('Tarefa não encontrada.')
    else:
        save_tasks(tasks_filtered)
        print('Tarefa deletada com sucesso.')

# Marca tarefa como "in-progress"
def mark_in_progress(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'in-progress'
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print('Tarefa marcada como em progresso.')
            return
    print('Tarefa não encontrada.')

# Marca tarefa como "done"
def mark_done(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'done'
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print('Tarefa marcada como concluída.')
            return
    print('Tarefa não encontrada.')

# Lista tarefas, com filtro opcional por status
def list_tasks(filter_status=None):
    tasks = load_tasks()
    if filter_status:
        tasks = [t for t in tasks if t['status'] == filter_status]
    if not tasks:
        print('Nenhuma tarefa encontrada.')
        return
    for task in tasks:
        print(f"ID: {task['id']} | Desc: {task['description']} | Status: {task['status']} | Criado: {task['createdAt']} | Atualizado: {task['updatedAt']}")

# Configuração do Argparse para CLI
def main():
    parser = argparse.ArgumentParser(prog='task-cli', description='Gerenciador de Tarefas (CLI)')
    subparsers = parser.add_subparsers(dest='command')

    # Subcomando: add
    parser_add = subparsers.add_parser('add', help='Adiciona uma nova tarefa')
    parser_add.add_argument('description', help='Descrição da tarefa')

    # Subcomando: update
    parser_update = subparsers.add_parser('update', help='Atualiza a descrição de uma tarefa')
    parser_update.add_argument('id', type=int, help='ID da tarefa')
    parser_update.add_argument('description', help='Nova descrição')

    # Subcomando: delete
    parser_delete = subparsers.add_parser('delete', help='Deleta uma tarefa')
    parser_delete.add_argument('id', type=int, help='ID da tarefa')

    # Subcomando: mark-in-progress
    parser_mip = subparsers.add_parser('mark-in-progress', help='Marca tarefa como em progresso')
    parser_mip.add_argument('id', type=int, help='ID da tarefa')

    # Subcomando: mark-done
    parser_md = subparsers.add_parser('mark-done', help='Marca tarefa como concluída')
    parser_md.add_argument('id', type=int, help='ID da tarefa')

    # Subcomando: list
    parser_list = subparsers.add_parser('list', help='Lista tarefas')
    parser_list.add_argument('status', nargs='?', choices=['todo', 'in-progress', 'done'], help='Filtrar por status')

    args = parser.parse_args()

    if args.command == 'add':
        add_task(args.description)
    elif args.command == 'update':
        update_task(args.id, args.description)
    elif args.command == 'delete':
        delete_task(args.id)
    elif args.command == 'mark-in-progress':
        mark_in_progress(args.id)
    elif args.command == 'mark-done':
        mark_done(args.id)
    elif args.command == 'list':
        list_tasks(args.status)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
