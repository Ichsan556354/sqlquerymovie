import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="movie_imdb"
)

cursor = connection.cursor()
