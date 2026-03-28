import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Jeetkunedo123!",
        database="construbrito"
    )