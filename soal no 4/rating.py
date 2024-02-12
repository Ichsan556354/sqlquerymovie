from connection import cursor

# Pertanyaan no 4b
query = """
    SELECT title, rating
    FROM movies
    WHERE rating >= 7.5
    ORDER BY rating DESC;
"""

cursor.execute(query)
result = cursor.fetchall()

print("Rating Film diatas 7.5: ")
for row in result:
    print("Nama     : ", row[0])
    print("Rating   : ", row[1])
    print()