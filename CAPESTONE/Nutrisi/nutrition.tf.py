import csv
import pandas as pd
import os


def hitung_total_nutrisi(file_path, jumlah_masukan):
    columns = ['VIt. A', 'Vit. B', 'Vit. C', 'Vit. D', 'Vit. E', 'Vit. K', 'Protein (g)', 'Mineral (%)', 'Energi (Kal)',
               'Lemak  (g)', 'Kalsium (mg)', 'Zat Besi (gr)', 'Serat (g)', 'Karbohidrad (gr)', 'Fosfor (mg)',
               'Magnesium (mg)', 'Natrium (mg)', 'Kalium (mg)']

    # Cek apakah file CSV yang berisi total nutrisi sudah ada
    if os.path.exists(file_path):
        df_total_nutrisi = pd.read_csv(file_path, index_col=0)
    else:
        df_total_nutrisi = pd.DataFrame(0, index=[0], columns=columns)

    for i in range(jumlah_masukan):
        print(f"\nMakanan ke-{i + 1}:")
        bahan_makanan_input = input("Masukkan nama bahan makanan: ")
        try:
            with open(r'D:\CAPESTONE\Nutrisi\nutrisi_fix.csv', 'r', encoding='utf-8') as file:
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
                    print(f"Bahan makan '{bahan_makanan_input}' tidak ditemukan dalam dataset nutrisi.")
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print("Terjadi kesalahan", str(e))

    # Simpan total nutrisi ke file CSV
    df_total_nutrisi.to_csv(file_path)

    return df_total_nutrisi


def identifikasi_kekurangan_nutrisi(umur_bayi, df_total_nutrisi):
    path_nutrisi_bayi = r'D:\CAPESTONE\Nutrisi\harian_fix.csv'

    df_nutrisi_bayi = pd.read_csv(path_nutrisi_bayi)

    nutrisi_bayi_dibutuhkan = df_nutrisi_bayi[df_nutrisi_bayi['Bulan'] == umur_bayi].iloc[0, 1:]
    nutrisi_terpenuhi = df_total_nutrisi.iloc[0]
    nutrisi_kurang = nutrisi_bayi_dibutuhkan - nutrisi_terpenuhi

    print("\nData Nutrisi:")
    for nutrisi, total in df_total_nutrisi.iloc[0].items():
        status = f"harian sudah terpenuhi" if nutrisi_kurang[
                                                  nutrisi] <= 0 else f"harian tidak terpenuhi sebanyak {nutrisi_kurang[nutrisi]}"
        print(f"{nutrisi} {total}, {nutrisi} harian {status}")


umur_bayi = int(input("Masukkan umur bayi dalam bulan: "))
if umur_bayi < 0 or umur_bayi > 36:
    print("Umur bayi tidak valid. Program berhenti.")
else:
    file_path = r'D:\CAPESTONE\Nutrisi\total_nutrisi.csv'
    jumlah_masukan = int(input("Masukkan jumlah bahan makanan yang ingin dimasukkan: "))
    df_total_nutrisi = hitung_total_nutrisi(file_path, jumlah_masukan)
    identifikasi_kekurangan_nutrisi(umur_bayi, df_total_nutrisi)
