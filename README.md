# Fraud Detection System

Este projeto treina e coloca em produção um modelo de detecção de fraude.

## Arquitetura da solução em produção

![Diagrama](imgs/diagrama.png)

## Curva AOC e Metricas do Modelo

![Curva ROC](model/metrics/roc_curve.png)

## Pré-requisitos

Certifique-se de ter o Docker  instalado na sua máquina. Se não tiver, siga as instruções abaixo:

### Instalação do Docker

- [Guia de Instalação do Docker](https://docs.docker.com/get-docker/)


## Clonando o Repositório

Para clonar este repositório, execute o seguinte comando:

```bash
git clone https://github.com/helio004/fraud-detect-system.git
cd fraud-detect-system
```

# Executando o Deploy Pipeline no Airflow

Para executar o deploy do pipeline de treinamento, utilizer o comando:

```bash
make run-pipeline
```

# Executando o Deploy

Para executar o deploy da API, utilizer o comando:

```bash
make run-api
```

Este comando ira construir e iniciar os contêineres Docker.

# Acessando o Airflow

Após o deploy, acesse a interface do Airflow na seguinte URL:

```bash
http://localhost:8080
```

Faça login Airflow (se necessário) e siga os próximos passos.

```
user: admin
password: admin
```
# Iniciando o Pipeline de Treinamento

1. No Airflow, encontre a DAG correspondente ao processo Pipeline.
2. Ative a DAG (ligue o botão ao lado do nome da DAG)
3. Inicie a DAG manualmente clicando no botão de "Trigger DAG".

![](imgs/airflow.png)

# Acessando o Modelo Treinado

Após a conclusão do pipeline de treinamento, você pode acessar o modelo treinado na seguinte URL: http://localhost:8000/docs


# Destruindo os Contêineres

```bash
make clean-env
```

Este projeto é licenciado sob os termos da [Licença MIT](./LICENSE)