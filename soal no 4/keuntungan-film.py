from connection import cursor

query = """
    SELECT title, budget, income
    FROM movies
    WHERE income > budget
    ORDER BY income - budget DESC;
"""

cursor.execute(query)
result = cursor.fetchall()
print("Film yang memiliki keuntungan: ")
for row in result:
    if row[1] != 0:
        print("Judul    : ", row[0])
        print("Modal    : $", '{:,.0f}'.format(row[1]).replace(',', '.'))
        print("Penghasilan  : $", '{:,.0f}'.format(row[2]).replace(',', '.'))
        print("Keuntungan   : $", '{:,.0f}'.format(row[2] - row[1]).replace(',', '.'))
        print()