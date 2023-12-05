import csv

def is_stunted(berat, panjang, kepala, data_berat, data_panjang, data_kepala):
    return (
        berat < data_berat[0] or berat > data_berat[1] or
        panjang < data_panjang[0] or panjang > data_panjang[1] or
        kepala < data_kepala[0] or kepala > data_kepala[1])
file_path = r'D:\Caps\Stunting\Dataset_New.csv'

jenis_kelamin = input("Masukkan jenis kelamin (Laki-laki/Perempuan): ")
umur_bulan = int(input("Masukkan umur bayi dalam bulan: "))
berat = float(input("Masukkan berat bayi (Kg): "))
panjang = float(input("Masukkan panjang bayi (Cm): "))
lingkar_kepala = float(input("Masukkan lingkar kepala bayi (Cm): "))

selected_data = []
with open(file_path, 'r') as file:
    csvreader = csv.DictReader(file)
    for row in csvreader:
        if row['Bulan'] == str(umur_bulan):
            data_berat = [float(row['batas bawah berat ideal']), float(row['batas atas berat ideal'])]
            data_panjang = [float(row['batas bawah panjang ideal']), float(row['batas atas panjang ideal'])]
            data_kepala = [float(row['batas bawah lingkar kepala ideal']), float(row['batas atas lingkar kepala ideal'])]

            if is_stunted(berat, panjang, lingkar_kepala, data_berat, data_panjang, data_kepala):
                print("stunting!")
            else:
                print("tidal stunting.")
            break
