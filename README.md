# Task-Tracker-CLI

(https://roadmap.sh/projects/task-tracker)

Este é um gerenciador de tarefas simples via linha de comando, desenvolvido em Python, que permite adicionar, atualizar, remover e acompanhar o status das suas tarefas através de um arquivo JSON.

## Funcionalidades

- **Adicionar tarefa**: `add "descrição"`
- **Atualizar descrição**: `update <id> "nova descrição"`
- **Remover tarefa**: `delete <id>`
- **Marcar em progresso**: `mark-in-progress <id>`
- **Marcar como concluída**: `mark-done <id>`
- **Listar tarefas**:
  - **Todas**: `list`
  - **Filtrar por status**: `list todo`, `list in-progress`, `list done`

Cada tarefa contém as propriedades:

- `id`: identificador único  
- `description`: descrição da tarefa  
- `status`: `todo`, `in-progress` ou `done`  
- `createdAt`: data/hora de criação (ISO 8601)  
- `updatedAt`: data/hora da última modificação (ISO 8601)  

## Como foi desenvolvido

- **Linguagem**: Python 3.x  
- **CLI**: built-in `argparse` para tratamento de argumentos  
- **Persistência**: arquivo `tasks.json` gerenciado com o módulo `json` e operações do sistema com `os`  
- **Data/Hora**: gerado com `datetime.now().isoformat()` para padronização  
- Não utiliza bibliotecas externas: apenas módulos nativos do Python.

## Instalação e uso

1. Garanta que o Python 3 esteja instalado:
   ```bash
   python --version

   No terminal, navegue até o diretório do projeto:

cd /caminho/para/task-tracker-cli
Execute o script com o comando desejado. Exemplos:


# Adicionar uma tarefa
python task_cli.py add "Comprar leite"

# Listar todas as tarefas
python task_cli.py list

# Marcar uma tarefa como em progresso
python task_cli.py mark-in-progress 1

# Atualizar tarefa
python task_cli.py update 1 "Comprar leite e pão"

# Marcar como concluída
python task_cli.py mark-done 1

# Listar tarefas concluídas
python task_cli.py list done
O arquivo tasks.json será criado automaticamente na primeira execução, se não existir.

Estrutura de arquivos

├── task_cli.py      # Script principal da CLI
├── tasks.json       # Base de dados de tarefas (gerado automaticamente)
└── README.md        # Documento de instruções (este arquivo)
Observações
Caso o tasks.json seja corrompido ou esteja com formato inválido, o script exibe mensagem de erro ao ler e continua com uma lista vazia.

Para manter a janela do terminal aberta ao usar duplo clique (Windows), pode-se adicionar ao final do arquivo:

input('Pressione Enter para encerrar...')
