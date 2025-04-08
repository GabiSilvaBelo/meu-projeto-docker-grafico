# 📊 Projeto Gráfico com Docker, Python, Pandas e Matplotlib

Este projeto foi criado para gerar um gráfico de barras simples a partir de um arquivo CSV, utilizando Python e bibliotecas populares de análise de dados — tudo isso dentro de um container Docker! 🐳

## 💻 Tecnologias usadas

- Python 3.10
- Pandas
- Matplotlib
- Docker

## 🗂 Estrutura do projeto

📁 meu_projeto_docker_grafico ├── grafico.py ├── dados.csv ├── requirements.txt ├── Dockerfile └── grafico.png ← gerado automaticamente após execução

## ⚙️ Como rodar com Docker

1. Clone o repositório:

```bash
git clone https://github.com/GabiSilvaBelo/meu-projeto-docker-grafico.git
cd meu-projeto-docker-grafico

2. Construa a imagem Docker:
docker build -t projeto-grafico .

3. Execute o container:
docker run -v $(pwd):/app projeto-grafico

4. O arquivo grafico.png será gerado na sua pasta. 🖼️

🧠 Objetivo

Este projeto foi desenvolvido como exercício prático de como usar Docker no dia a dia de Ciência de Dados para:

Automatizar ambientes
Compartilhar projetos facilmente com o time
Aprender conceitos de reprodutibilidade

✨ Autor(a) Feito com 💜 por Gabriela Belo da Silva
