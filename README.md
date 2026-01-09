# Data Pipeline with the GoRest API

Este projeto foi desenvolvido para aprofundar meus conhecimentos em Engenharia de Dados, com foco principal no consumo e manipulação de APIs RESTful. O objetivo era ir além da simples extração de dados e praticar todo o ciclo de vida da interação com uma API, utilizando a biblioteca `requests` para explorar os diferentes conceitos, como autenticação e métodos HTTP (GET, POST, PUT, PATCH e DELETE).

Como resultado prático, o projeto implementa um pipeline ETL simples que extrai os dados, transforma-os para atender a diferentes casos de uso e os carrega em arquivos CSV, prontos para análise.

---

## Tecnologias Utilizadas ⚒️

*   **Linguagem:** Python
*   **Bibliotecas:**
    *   `requests`: Para realizar as chamadas HTTP e interagir com a API GoRest.
    *   `pandas`: Para estruturar, transformar e manipular os dados.
    *   `python-dotenv`: Para gerenciar as chaves de API de forma segura.
*   **Ambiente de Desenvolvimento:** Jupyter Notebook

## Estrutura do Projeto

-   `src/study_api.ipynb`: Um notebook Jupyter contendo o estudo detalhado de cada método HTTP.
-   `src/pipeline.ipynb`: O script Python final que executa o pipeline de dados de ponta a ponta.
-   `requirements.txt`: Lista de dependências do projeto para fácil instalação.
-   `.env`: Arquivo local para armazenar o token de autenticação (ignorado pelo Git).
-   `data/`: Pasta onde os arquivos CSV gerados são salvos (ignorada pelo Git).

## Como Executar

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/RenanAbreuC/pipeline-api-gorest.git
    cd pipeline-api-gorest
    ```
2.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Configure seu Token:**
    *   Crie um arquivo chamado `.env` na raiz do projeto.
    *   Adicione seu token da GoRest a ele, no seguinte formato:
        ```
        API_TOKEN="seu_token_aqui"
        ```
4.  **Execute os Notebooks:**
    *   Abra a pasta do projeto no VS Code ou inicie o Jupyter.
    *   Execute as células em `api_study.ipynb` para ver o estudo dos métodos da API.
    *   Execute as células em `pipeline.ipynb` para gerar os arquivos CSV na pasta `data/`.
