# Use a imagem base do Python 3.8
FROM python:3.12.0

# Configuração de variáveis de ambiente
ENV PYTHONUNBUFFERED 1

# Criação do diretório de trabalho
WORKDIR /app

# Copia os arquivos necessários para o diretório de trabalho
COPY . /app/

# Instalação das dependências do projeto
RUN pip install -r requirements.txt

# Comando para iniciar o aplicativo usando Gunicorn
CMD ["gunicorn", "pixelhub_app.wsgi:application", "--bind", "0.0.0.0:8000"]


