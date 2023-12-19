import csv
import pandas as pd
import random


def hitung_total_nutrisi():
    file_path = r'D:\CAPESTONE\Nutrisi\dataset numerik.csv'

    # Definisi kolom nutrisi
    columns = ['VIt. A', 'Vit. B', 'Vit. C', 'Vit. D', 'Vit. E', 'Vit. K', 'Protein (g)', 'Mineral (%)', 'Energi (Kal)',
               'Lemak  (g)', 'Kalsium (mg)', 'Zat Besi (gr)', 'Serat (g)', 'Karbohidrad (gr)', 'Fosfor (mg)',
               'Magnesium (mg)', 'Natrium (mg)', 'Kalium (mg)']

    # Membuat DataFrame untuk total nutrisi
    df_total_nutrisi = pd.DataFrame(0, index=[0], columns=columns)

    umur_bayi = random.randint(0, 36)
    jumlah_masukan = random.randint(1, 10)

    bahan_makanan_list = []
    for _ in range(jumlah_masukan):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                csv_reader = csv.DictReader(file)
                random_row = random.choice(list(csv_reader))
                bahan_makanan_input = random_row['Bahan Makan']
                bahan_makanan_list.append(bahan_makanan_input)
                df_input = pd.DataFrame([random_row])
                df_input = df_input.apply(pd.to_numeric, errors='coerce').fillna(0)
                df_total_nutrisi += df_input
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print("Terjadi kesalahan", str(e))

    return umur_bayi, df_total_nutrisi, jumlah_masukan, bahan_makanan_list


def identifikasi_kekurangan_nutrisi(umur_bayi, df_total_nutrisi, jumlah_masukan, bahan_makanan_list):
    path_nutrisi_bayi = r'D:\CAPESTONE\Nutrisi\dataset_harian.csv'

    df_nutrisi_bayi = pd.read_csv(path_nutrisi_bayi)

    nutrisi_bayi_dibutuhkan = df_nutrisi_bayi[df_nutrisi_bayi['Bulan'] == umur_bayi].iloc[0, 1:]

    nutrisi_terpenuhi = df_total_nutrisi.iloc[0]
    nutrisi_kurang = nutrisi_bayi_dibutuhkan - nutrisi_terpenuhi

    output_data = {
        'Umur': umur_bayi,
        'Jumlah Masukan': jumlah_masukan,
        'Bahan Makanan': ', '.join(bahan_makanan_list),
        'Nutrisi Tidak Terpenuhi': ', '.join([nutrisi for nutrisi, kurang in nutrisi_kurang.items() if kurang > 0])
    }
    output_csv_path = r'D:\CAPESTONE\Nutrisi\new\new_data_train.csv'
    try:
        with open(output_csv_path, 'a', newline='') as output_csv:
            csv_writer = csv.DictWriter(output_csv, fieldnames=output_data.keys())
            csv_writer.writerow(output_data)
    except FileNotFoundError:
        with open(output_csv_path, 'w', newline='') as output_csv:
            csv_writer = csv.DictWriter(output_csv, fieldnames=output_data.keys())
            csv_writer.writeheader()
            csv_writer.writerow(output_data)

    print(f"\nData appended to CSV: {output_csv_path}")


for _ in range(1000):
    umur_bayi, df_total_nutrisi, jumlah_masukan, bahan_makanan_list = hitung_total_nutrisi()
    identifikasi_kekurangan_nutrisi(umur_bayi, df_total_nutrisi, jumlah_masukan, bahan_makanan_list)
