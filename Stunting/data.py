import csv
import random

def is_stunted(berat, panjang, kepala, data_berat, data_panjang, data_kepala):
    return (
        berat < data_berat[0] or berat > data_berat[1] or
        panjang < data_panjang[0] or panjang > data_panjang[1] or
        kepala < data_kepala[0] or kepala > data_kepala[1]
    )

file_path_input = r'D:\CAPESTONE\Stunting\bersih.csv'
file_path_output = r'D:\CAPESTONE\Stunting\data_train.csv'

random_entries = []
for _ in range(1000000):
    jenis_kelamin = random.choice(["Laki-laki", "Perempuan"])
    umur_bulan = random.randint(0, 24)
    berat = round(random.uniform(2.0, 8.0), 2)
    panjang = round(random.uniform(30.0, 70.0), 2)
    lingkar_kepala = round(random.uniform(20.0, 50.0), 2)

    selected_data = []

    with open(file_path_input, 'r') as file:
        csvreader = csv.DictReader(file)
        for row in csvreader:
            if row['umur'] == str(umur_bulan):
                data_berat = [float(row['batas bawah berat']), float(row['batas atas berat'])]
                data_panjang = [float(row['batas bawah panjang']), float(row['batas atas panjang'])]
                data_kepala = [float(row['batas bawah kepala']), float(row[
