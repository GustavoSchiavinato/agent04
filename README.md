# Criando um Agente para Automatizar Fluxos de Trabalho no Trello

# 🚀 Criando um Agente para Automatizar Fluxos de Trabalho no Trello

Este guia descreve como configurar um agente para organizar e automatizar tarefas no **Trello**, integrando-o ao seu ambiente de desenvolvimento.

---

## 📌 01 - Preparando o Trello para a integração com o agente
- Crie um **Board** no Trello para centralizar suas tarefas.
- Configure **listas** (ex.: "A Fazer", "Em Andamento", "Concluído").
- Gere uma **API Key** e um **Token** de acesso no [Trello Developer](https://trello.com/app-key).
- Anote o **ID do Board** e das listas, pois serão usados pelo agente.

---

## 🛠️ 02 - Criando e configurando o ambiente virtual
- Instale o Python (>= 3.9).
- Crie um ambiente virtual:
  ```bash
  python -m venv venv
  source venv/bin/activate   # Linux/Mac
  venv\Scripts\activate      # Windows

- Instale as dependências necessárias:
- pip install requests python-dotenv

---

## 🤖 03 - Configurando o agente organizador de tarefas
- Crie um arquivo .env com suas credenciais:
TRELLO_API_KEY=xxxx
TRELLO_TOKEN=xxxx
TRELLO_BOARD_ID=xxxx

- Implemente um módulo agent.py que:
- Conecte-se à API do Trello.
- Liste e organize tarefas.
- Automatize movimentações entre listas.

---

## 📝 04 - Criando e listando tarefas no Trello via agente
Exemplo de criação de tarefa:
import requests, os

API_KEY = os.getenv("TRELLO_API_KEY")
TOKEN = os.getenv("TRELLO_TOKEN")
BOARD_ID = os.getenv("TRELLO_BOARD_ID")
LIST_ID = "ID_DA_LISTA_A_FAZER"

url = f"https://api.trello.com/1/cards"
query = {
    'key': API_KEY,
    'token': TOKEN,
    'idList': LIST_ID,
    'name': "Nova tarefa automatizada"
}

response = requests.post(url, params=query)
print(response.json())

Exemplo de listagem de tarefas:

url = f"https://api.trello.com/1/boards/{BOARD_ID}/cards"
query = {'key': API_KEY, 'token': TOKEN}
response = requests.get(url, params=query)
for card in response.json():
    print(card['name'])

---

## 🔄 05 - Automatizando a movimentação de tarefas no Trello
Para mover uma tarefa entre listas:
CARD_ID = "ID_DA_TAREFA"
NEW_LIST_ID = "ID_DA_LISTA_EM_ANDAMENTO"

url = f"https://api.trello.com/1/cards/{CARD_ID}"
query = {
    'key': API_KEY,
    'token': TOKEN,
    'idList': NEW_LIST_ID
}

response = requests.put(url, params=query)
print("Tarefa movida com sucesso!")

---

## ✅ Conclusão
Com este agente, você pode:
• 	Criar tarefas automaticamente.
• 	Listar e organizar atividades.
• 	Movimentar tarefas entre listas sem precisar acessar manualmente o Trello.
Isso abre espaço para fluxos de trabalho inteligentes, integrando o Trello com outros sistemas e aumentando a produtividade.

