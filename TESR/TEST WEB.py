import csv
import tkinter as tk
from tkinter import Label, Entry, Button


def is_stunted(berat, panjang, kepala, data_berat, data_panjang, data_kepala):
    return (
            berat < data_berat[0] or berat > data_berat[1] or
            panjang < data_panjang[0] or panjang > data_panjang[1] or
            kepala < data_kepala[0] or kepala > data_kepala[1])


def check_stunting(berat, panjang, kepala, data_berat, data_panjang, data_kepala):
    with open(file_path, 'r') as file:
        csvreader = csv.DictReader(file)

        print(csvreader.fieldnames)
        for row in csvreader:
            try:
                if row['Bulan'] == str(umur_bulan) and row['Jenis Kelamin'] == jenis_kelamin:
                    data_berat = [float(row['batas bawah berat ideal']), float(row['batas atas berat ideal'])]
                    data_panjang = [float(row['batas bawah panjang ideal']), float(row['batas atas panjang ideal'])]
                    data_kepala = [float(row['batas bawah lingkar kepala ideal']), float(row['batas atas lingkar kepala ideal'])]

                    result_label.config(
                        text=f"Output:\nBulan: {umur_bulan}, Berat: {berat}, Panjang: {panjang}, Lingkar Kepala: {kepala}")

                    if is_stunted(berat, panjang, kepala, data_berat, data_panjang, data_kepala):
                        result_label.config(text=result_label.cget("text") + "\nStatus: Stunting!")
                    else:
                        result_label.config(text=result_label.cget("text") + "\nStatus: Tidak Stunting.")
                    break
            except KeyError:
                result_label.config(text="salah input")
                break


def on_male_button_click():
    global jenis_kelamin, umur_bulan, data_berat, data_panjang, data_kepala
    jenis_kelamin = "Laki-laki"
    umur_bulan = int(umur_entry.get())
    berat = float(berat_entry.get())
    panjang = float(panjang_entry.get())
    kepala = float(kepala_entry.get())
    check_stunting(berat, panjang, kepala, data_berat, data_panjang, data_kepala)


def on_female_button_click():
    global jenis_kelamin, umur_bulan, data_berat, data_panjang, data_kepala
    jenis_kelamin = "Perempuan"
    umur_bulan = int(umur_bulan_entry.get())
    berat = float(berat_entry.get())
    panjang = float(panjang_entry.get())
    kepala = float(kepala_entry.get())
    check_stunting(berat, panjang, kepala, data_berat, data_panjang, data_kepala)


file_path = r'D:\Caps\Stunting\Dataset_New.csv'

# Create the main window
window = tk.Tk()
window.title("Stunting Checker")

# Create entry widgets with labels
umur_label = Label(window, text="Umur (bulan):")
umur_label.pack(pady=5)
umur_entry = Entry(window, width=10)
umur_entry.pack(pady=5)

berat_label = Label(window, text="Berat (Kg):")
berat_label.pack(pady=5)
berat_entry = Entry(window, width=10)
berat_entry.pack(pady=5)

panjang_label = Label(window, text="Panjang (Cm):")
panjang_label.pack(pady=5)
panjang_entry = Entry(window, width=10)
panjang_entry.pack(pady=5)

kepala_label = Label(window, text="Lingkar Kepala (Cm):")
kepala_label.pack(pady=5)
kepala_entry = Entry(window, width=10)
kepala_entry.pack(pady=5)

# Create buttons
male_button = Button(window, text="Laki-laki", command=on_male_button_click)
male_button.pack(pady=10)
female_button = Button(window, text="Perempuan", command=on_female_button_click)
female_button.pack(pady=10)

# Create a label to display the result
result_label = Label(window, text="")
result_label.pack(pady=10)

# Run the main loop
window.mainloop()
