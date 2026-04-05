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
