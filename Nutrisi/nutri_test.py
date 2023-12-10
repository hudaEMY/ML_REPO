import csv
import pandas as pd

file_path = r'D:\CAPESTONE\Nutrisi\NTS.csv'

columns = ['VIt. A', 'Vit. B', 'Vit. C', 'Vit. D', 'Vit. E', 'Vit. K', 'Protein (g)', 'Mineral (%)', 'Energi (Kal)', 'Lemak  (g)', 'Kalsium (mg)', 'Zat Besi (gr)', 'Serat (g)', 'protein (gr)']
df_total_nutrisi = pd.DataFrame(0, index=[0], columns=columns)

jumlah_masukan = int(input("Masukkan jumlah bahan makanan yang ingin dimasukkan: "))
for i in range(jumlah_masukan):
    print(f"\nMakanan ke-{i + 1}:")
    bahan_makanan_input = input("Masukkan nama bahan makanan: ")
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            found = False
            for row in csv_reader:
                if row['Bahan Makan'].lower() == bahan_makanan_input.lower():
                    found = True
                    df_input = pd.DataFrame([row])
                    df_input = df_input.apply(pd.to_numeric, errors='coerce').fillna(0)
                    df_total_nutrisi += df_input
                    break
            if not found:
                print(f"Bahan baku '{bahan_makanan_input}' tidak ditemukan dalam dataset nutrisi.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("Terjadi kesalahan", str(e))

print("\nTotal Nutrisi Harian dari Bahan Makanan yang Dimasukkan:")
df_total_nutrisi_transposed = df_total_nutrisi.transpose()
for index, value in df_total_nutrisi_transposed.iterrows():
    print(f"{index} = {value[0]}")
