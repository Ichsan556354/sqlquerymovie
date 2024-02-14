from connection import cursor

# Pertanyaan no 4b
query = """
    SELECT title, directors
FROM movies
WHERE rating > 7.5
GROUP BY directors
HAVING COUNT(*) > 1;
"""

cursor.execute(query)
result = cursor.fetchall()

print("Rating Film diatas 7.5: ")
for row in result:
    print("Nama Film    : ", row[0])
    print("Nama Sutradara: ", row[1])
    print()