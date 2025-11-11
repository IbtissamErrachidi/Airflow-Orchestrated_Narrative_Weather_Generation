FROM apache/airflow:2.9.3

# Copier requirements.txt
COPY requirements.txt /tmp/requirements.txt

# Installer les dépendances Python en tant qu'utilisateur airflow
USER airflow
RUN pip install --no-cache-dir -r /tmp/requirements.txt
