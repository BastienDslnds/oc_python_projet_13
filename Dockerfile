# image initiale
FROM python:3.11 as python

# On s'assure que la sortie stardard de python n'utilise pas de tampon et
# s'affiche directement.
ENV PYTHONUNBUFFERED 1
# On désire pas que python crée des fichiers *.pyc
ENV PYTHONDONTWRITEBYTECODE 1

# Définition du répertoire de travail
WORKDIR /app

# Installation des dépendances python dans le conteneur
RUN pip install --upgrade pip 
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# On copie tout le contenu du répertoire courant dans /app
COPY . /app

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]