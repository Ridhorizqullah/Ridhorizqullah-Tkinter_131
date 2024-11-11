import tkinter as tk #Mengimpor seluruh modul tkinter dan memberi alias tk.
from tkinter import messagebox #Mengimpor modul messagebox dari pustaka tkinter.

# Fungsi untuk memvalidasi input dan menampilkan hasil prediksi
def hasil_prediksi():
    try:
        # Memeriksa setiap input untuk memastikan nilainya valid (0-100)
        for entry in input_entries:
            nilai = int(entry.get())  # Mengambil nilai dari input
            if not (0 <= nilai <= 100):
                raise ValueError("Nilai harus antara 0 dan 100.")
        
        # Menampilkan hasil prediksi (selalu Teknologi Informasi)
        output_label.config(text="Prodi Pilihan: Teknologi Informasi")
    except ValueError:
        # Menampilkan pesan error jika ada input yang tidak valid
        messagebox.showerror("Input Error", "Pastikan semua input adalah antara 0 dan 100.")

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")  # Judul aplikasi
root.geometry("500x600")  # Ukuran jendela aplikasi
root.configure(bg="#0077be")  # Mengatur warna latar belakang biru laut

# Label judul aplikasi
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16), bg="#0077be", fg="white")
judul_label.grid(row=0, column=0, columnspan=2, pady=10)

# Daftar mata pelajaran yang akan diinputkan
mata_pelajaran = ["Matematika", "Bahasa Indonesia", "Bahasa Inggris", "Fisika", "Kimia", 
                  "Biologi", "Ekonomi", "Geografi", "Sejarah", "Sosiologi"]

# Mengonfigurasi kolom agar fleksibel
root.columnconfigure(0, weight=1) 
root.columnconfigure(1, weight=1)

# Membuat input untuk nilai mata pelajaran
input_labels = []  # Menyimpan label input
input_entries = []  # Menyimpan field input

# Loop untuk membuat label dan input untuk setiap mata pelajaran
for i, pelajaran in enumerate(mata_pelajaran):
    input_label = tk.Label(root, text=f"Nilai {pelajaran}:", bg="#0077be", fg="white")  # Label nama pelajaran
    input_entry = tk.Entry(root)  # Field input untuk nilai
    input_label.grid(row=i + 1, column=0, padx=10, pady=5, sticky="e")  # Menempatkan label di grid
    input_entry.grid(row=i + 1, column=1, padx=10, pady=5)  # Menempatkan input di grid
    input_labels.append(input_label)  # Menambahkan label ke daftar
    input_entries.append(input_entry)  # Menambahkan entry ke daftar

# Tombol untuk melakukan prediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi, bg="#0077be", fg="white")
prediksi_button.grid(row=11, column=0, columnspan=2, pady=10)

# Label untuk menampilkan hasil prediksi
output_label = tk.Label(root, text="Prodi Pilihan: ", font=("Arial", 12), bg="#0077be", fg="white")
output_label.grid(row=12, column=0, columnspan=2, pady=10)

# Menjalankan loop utama aplikasi
root.mainloop()
