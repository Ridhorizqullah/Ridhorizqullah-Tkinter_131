import tkinter as tk
from tkinter import messagebox

# Fungsi untuk memvalidasi input dan menampilkan hasil prediksi
def hasil_prediksi():
    try:
        for entry in input_entries:
            nilai = int(entry.get())
            if not (0 <= nilai <= 100):
                raise ValueError("Nilai harus antara 0 dan 100.")
        output_label.config(text="Prodi Pilihan: Prediksi berhasil")  # Placeholder hasil prediksi
    except ValueError:
        messagebox.showerror("Input Error", "Pastikan semua input adalah antara 0 dan 100.")

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")

# Mengatur ukuran dan posisi jendela di tengah layar
window_width = 500
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_x = (screen_width - window_width) // 2
position_y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
root.configure(bg="#e0f7fa")  # Mengubah warna latar belakang menjadi biru muda

# Mengatur konfigurasi grid agar konten di tengah
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

# Label judul
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16), bg="#e0f7fa", fg="#00796b")
judul_label.grid(row=0, column=0, columnspan=2, pady=20, sticky="n")

# Daftar nama mata pelajaran
mata_pelajaran = ["Matematika", "Bahasa Indonesia", "Bahasa Inggris", "Fisika", "Kimia", 
                  "Biologi", "Ekonomi", "Geografi", "Sejarah", "Sosiologi"]

# Membuat input untuk nilai mata pelajaran
input_entries = []

for i, pelajaran in enumerate(mata_pelajaran):
    input_label = tk.Label(root, text=f"Nilai {pelajaran}:", bg="#e0f7fa", fg="#004d40")
    input_entry = tk.Entry(root)
    
    input_label.grid(row=i + 1, column=0, padx=10, pady=5, sticky="e")
    input_entry.grid(row=i + 1, column=1, padx=10, pady=5, sticky="w")
    input_entries.append(input_entry)

# Tombol Hasil Prediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi, bg="#00796b", fg="white")
prediksi_button.grid(row=len(mata_pelajaran) + 1, column=0, columnspan=2, pady=20)

# Label untuk menampilkan hasil
output_label = tk.Label(root, text="Prodi Pilihan: ", font=("Arial", 12), bg="#e0f7fa", fg="#00796b")
output_label.grid(row=len(mata_pelajaran) + 2, column=0, columnspan=2, pady=20)

# Mengatur row dan column agar mengisi ruang yang tersedia
for i in range(len(mata_pelajaran) + 3):  # +3 untuk judul, tombol, dan hasil
    root.rowconfigure(i, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

# Menjalankan loop utama aplikasi
root.mainloop()