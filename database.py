import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host="localInstances2",
        user="root",
        password="Ajitha@444",
        database="saams"
    )
    return connection
