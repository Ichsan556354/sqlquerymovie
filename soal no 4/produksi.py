from connection import cursor

query = """SELECT month, COUNT(*) AS Jumlah_Film_Diproduksi
FROM movies
GROUP BY month
ORDER BY Jumlah_Film_Diproduksi DESC
LIMIT 1;
"""

cursor.execute(query)
results = cursor.fetchall()

print("Pengelompokkan Data berdasarkan Sertifikat Film")
for row in results:
    print(row[0], "-", row[1], "movies")
