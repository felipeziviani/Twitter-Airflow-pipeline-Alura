# 🐦 Twitter Data Pipeline com Apache Airflow

Projeto desenvolvido durante curso da **Alura**, com o objetivo de
construir um pipeline de dados utilizando **Apache Airflow** para
extração e armazenamento de dados do Twitter.

------------------------------------------------------------------------

## 📌 Objetivo

Criar um pipeline automatizado que:

-   Coleta dados do Twitter com base em uma query\
-   Armazena os dados em formato JSON\
-   Organiza os dados em um Data Lake\
-   Executa de forma agendada com Airflow

------------------------------------------------------------------------

## Estrutura do Projeto

    airflow_pipeline/
    │
    ├── dags/
    │   ├── twitter_dag.py
    │   ├── operators/
    │   │   └── twitter_operator.py
    │   └── hook/
    │       └── twitter_hook.py
    │
    ├── datalake/
    │   └── twitter_datascience/
    │
    └── README.md

------------------------------------------------------------------------

## Tecnologias Utilizadas

-   Python\
-   Apache Airflow\
-   Airflow HTTP Hook\
-   JSON

------------------------------------------------------------------------

## Funcionamento do Pipeline

O DAG `twitter_dag`:

-   Executa diariamente (`@daily`)\
-   Busca tweets com a query `"datascience"`\
-   Coleta dados do dia anterior\
-   Armazena os dados no Data Lake

### Exemplo de saída

    datalake/twitter_datascience/
    └── extract_date=2026-01-10/
        └── datascience_20260110.json

------------------------------------------------------------------------

## Agendamento

-   Frequência: diária\
-   `catchup`: desativado\
-   Data de início: 01/01/2026

------------------------------------------------------------------------

## Como Executar

### 1. Criar ambiente virtual

``` bash
python -m venv venv
source venv/bin/activate
```

### 2. Instalar dependências

``` bash
pip install apache-airflow
```

### 3. Rodar o Airflow

``` bash
airflow standalone
```

### 4. Acessar interface

http://localhost:8080

### 5. Ativar a DAG

-   Procurar por: `twitter_dag`\
-   Ativar no toggle

------------------------------------------------------------------------

## Conceitos Aplicados

-   DAGs (Directed Acyclic Graphs)\
-   Operators customizados\
-   Hooks no Airflow\
-   Templates com Jinja (`{{ ds }}`, `macros`)\
-   Organização de Data Lake

------------------------------------------------------------------------

## Referência

Projeto baseado no curso da Alura:

> Apache Airflow: extração de dados



