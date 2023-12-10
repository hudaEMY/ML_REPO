import pandas as pd

path_nutrisi_bayi = r'D:\CAPESTONE\Nutrisi\harian_fix.csv'

df_nutrisi_bayi = pd.read_csv(path_nutrisi_bayi)
umur_bayi = int(input("Masukkan umur bayi dalam bulan (0-36): "))
if umur_bayi < 0 or umur_bayi > 36:
    print("Umur bayi tidak valid. Program berhenti.")
    exit()

input_nutrisi = {}
for nutrisi in df_nutrisi_bayi.columns[1:]:
    input_nutrisi[nutrisi] = float(input(f"Masukkan nilai {nutrisi} untuk bayi (dalam gram/mg): "))

df_input_nutrisi = pd.DataFrame(input_nutrisi, index=[0])

nutrisi_bayi_dibutuhkan = df_nutrisi_bayi[df_nutrisi_bayi['Bulan'] == umur_bayi].iloc[0, 1:]
nutrisi_terpenuhi = df_input_nutrisi.iloc[0]
nutrisi_kurang = nutrisi_bayi_dibutuhkan - nutrisi_terpenuhi

print("\nAnalisis Nutrisi yang Belum Terpenuhi:")
for nutrisi, kurang in nutrisi_kurang.items():
    if kurang > 0:
        print(f"{nutrisi} kurang terpenuhi sebanyak {kurang}")
    else:
        print(f"{nutrisi} sudah terpenuhi")
