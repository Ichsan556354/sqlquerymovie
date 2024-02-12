from connection import cursor

# Query SQL untuk mendapatkan 5 film dengan rating tertinggi untuk setiap bulan
query = """
    SELECT Month, Title, Rating
    FROM movies
    WHERE (Month, Rating) IN (
        SELECT Month, MAX(Rating)
        FROM movies
        GROUP BY Month
    )
    ORDER BY Month, Rating
"""

# Menjalankan query
cursor.execute(query)
results = cursor.fetchall()

# Menampilkan hasil
for row in results:
    print("Bulan:", row[0])
    print("Judul Film:", row[1])
    print("Rating:", row[2])
    print()