import csv

file_path = r'D:\Caps\Nutrisi\NTS.csv'

bahan_makanan_input = input("Masukkan nama bahan makanan: ")

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)

        found = False
        for row in csv_reader:
            if row['Bahan Makan'].lower() == bahan_makanan_input.lower():
                found = True
                print("\nInformasi Nutrisi untuk '{}' per 100 gramnya:".format(bahan_makanan_input))
                print("Vitamin A: {}".format(row['VIt. A']))
                print("Vitamin B: {}".format(row['Vit. B']))
                print("Vitamin C: {}".format(row['Vit. C']))
                print("Vitamin D: {}".format(row['Vit. D']))
                print("Vitamin E: {}".format(row['Vit. E']))
                print("Vitamin K: {}".format(row['Vit. K']))
                print("Protein: {} gram".format(row['Protein (g)']))
                print("Mineral: {}%".format(row['Mineral (%)']))
                print("Energi: {} Kal".format(row['Energi (Kal)']))
                print("Lemak: {} gram".format(row['Lemak  (g)']))
                print("Kalsium: {} mg".format(row['Kalsium (mg)']))
                print("Zat Besi: {} gr".format(row['Zat Besi (gr)']))
                print("Serat: {} gram".format(row['Serat (g)']))
                print("BELUM BUAT DATA KARBO!")
                break

        if not found:
            print("Bahan '{}' tidak ditemukan dalam dataset nutrisi.".format(bahan_makanan_input))

except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("Terjadi kesalahan", str(e))
