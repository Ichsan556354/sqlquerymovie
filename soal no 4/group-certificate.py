from connection import cursor

# pertanyaan 4a
query = """
    SELECT certificate, COUNT(*) AS TotalMovies
    FROM movies
    GROUP BY certificate;
"""
cursor.execute(query)
results = cursor.fetchall()

print("Pengelompokkan Data berdasarkan Sertifikat Film")
for row in results:
    print(row[0], "-", row[1], "movies")
