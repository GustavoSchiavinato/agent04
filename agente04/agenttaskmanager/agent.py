from google.adk.agents.llm_agent import Agent
from trello import trelloclient
from dotenv import load_dotenv
from datetime import datetime
import os

load_dotenv()

API_KEY = os.getenv('TRELLO_API_KEY')
API_SECRET = os.getenv('TRELLO_API_SECRET')
TOKEN = os.getenv('TRELLO_TOKEN')

def get_temporal_context():
  now = datetime.now()
  return now.strftime('%Y/%m/%d %H:%M:%S')

def adicionar_tarefa(nome_da_task: str, descricao_da_task: str, due_date: str):

  client = trelloclient(
    api_key=API_KEY
    api_secret=API_SECRET
    token=TOKEN
  )

  client.list_boards()
  boards = client.list_boards()
  meu_board = [b for b in boards if b.name == 'DIO'][0]

  listas = meu_board.list_lists()

  minha_lista = [l for l in listas if l.name.upper() == 'TO DO' or l.name.upper() == 'A FAZER'][0]

  minha_lista.add_card(
    name=nome_da_task,
    desc=descricao_da_task,
    due=due_date
  )


root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='Agente de Organização de Tarefas.',
    instruction="""Você é um agente de organização de tarefas.
                Sua função é receber um tarefa e criar um card no Trello com o nome e descrição da tarefa.
                Você deve perguntar as atividades que tenho no dia e criar um card para cada uma delas.
                Você inicia a conversa assim que for ativado, perguntando quais são as tarefas do dia.
                Sempre inicie a conversa perguntando quais são as tarefas do dia informando a data com pela tool get_temporal_context,
                e depois vá perguntando se tem mais alguma tarefa, até que o usuário diga que não tem mais tarefas.
                Suas Funções:
                1. Adicionar novas tarefas com nome e descrição.
                 2. Listar todas as tarefas ou filtrar por status.
                  3. Marcas as tarefas concluídas.
                  4. Remover tarefas da lista.
                  5. Mudar o status de tarefas (Ex.: "A fazer" para "Em Andamento" e de "Em Andamento" para "Concluído")
                  6. Criar contexto temporal (Data e hora atual) para organizar as tarefas do dia""",

    tools=[adicionar_tarefa, get_temporal_context],
)
