FROM mysql:latest

# Définir les variables d'environnement pour MySQL
ENV MYSQL_ROOT_PASSWORD=rootpassword
ENV MYSQL_DATABASE=mydatabase
ENV MYSQL_USER=myuser
ENV MYSQL_PASSWORD=mypassword

# Copier un script SQL pour initialiser la base de données (optionnel)
# COPY init.sql /docker-entrypoint-initdb.d/

# Exposer le port MySQL
EXPOSE 3306

# Commande de démarrage
CMD ["mysqld"]