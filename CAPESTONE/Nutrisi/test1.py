import tensorflow as tf
import pandas as pd

def hitung_total_nutrisi():
    file_path = 'nutrisi_fix.csv'  # Ganti dengan path file CSV Anda

    # Membuat DataFrame untuk menyimpan total nutrisi
    df_total_nutrisi = None

    jumlah_masukan = int(input("Masukkan jumlah bahan makanan yang ingin dimasukkan: "))
    for i in range(jumlah_masukan):
        print(f"\nMakanan ke-{i + 1}:")
        bahan_makanan_input = input("Masukkan nama bahan makanan: ")

        # Membaca file CSV dengan TensorFlow
        record_defaults = [tf.string] + [tf.float32]*18  # Sesuaikan dengan jumlah kolom Anda
        dataset = tf.data.experimental.CsvDataset(file_path, record_defaults=record_defaults, header=True)

        # Mencari bahan makanan dalam dataset
        found = False
        for row in dataset:
            if row[0].numpy().decode('utf-8').lower() == bahan_makanan_input.lower():
                found = True
                if df_total_nutrisi is None:
                    df_total_nutrisi = pd.DataFrame([row[1:].numpy()], columns=row[0].numpy())
                else:
                    df_total_nutrisi += pd.DataFrame([row[1:].numpy()], columns=row[0].numpy())
                break

    return df_total_nutrisi

df_total_nutrisi = hitung_total_nutrisi()
print("\nTotal Nutrisi:")
print(df_total_nutrisi)
