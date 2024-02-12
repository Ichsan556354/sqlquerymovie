import csv

def clean_data(input_file, output_file):
    with open(input_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Melewatkan baris header

        cleaned_data = []

        for row in reader:
            # Memastikan setiap baris memiliki jumlah kolom yang sesuai
            if len(row) == 13:
                # Menghapus spasi ekstra dan tanda kutip ganda yang berlebihan
                row = [entry.strip().replace('"', '') for entry in row]
                # Mengubah nilai Budget dan Income menjadi integer
                row[10] = int(row[10].replace('$', '').replace(',', ''))
                row[11] = int(row[11].replace('$', '').replace(',', ''))
                # Menambahkan baris yang telah dibersihkan ke dalam cleaned_data
                cleaned_data.append(row)
            else:
                print("Error: Baris data tidak lengkap:", row)

    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # Menulis header
        writer.writerow(["Title", "Rating", "Year", "Month", "Certificate", "Runtime", "Directors", "Stars", "Genre", "Filming_location", "Budget", "Income", "Country_of_origin"])
        # Menulis setiap baris data yang telah dibersihkan
        writer.writerows(cleaned_data)

# Memanggil fungsi clean_data dengan nama file input dan output
clean_data("data/movies.csv", "cleaned_movies_data.csv")
