import os
import sys
import time
from google.colab import files
from IPython.display import Audio, display

# Pastikan folder /mnt/data/ ada
data_path = "/mnt/data/"
if not os.path.exists(data_path):
    os.makedirs(data_path)

# Cek apakah ada file lagu yang sudah diunggah
audio_file = None

# 1. Unggah file jika belum ada
if not any(fname.endswith(".mp3") for fname in os.listdir(data_path)):
    print("File tidak ditemukan! Harap unggah ulang.")
    uploaded = files.upload()

    # Dapatkan nama file yang diunggah secara otomatis
    for filename in uploaded.keys():
        audio_file = os.path.join(data_path, filename)
        os.rename(filename, audio_file)
else:
    # Ambil file mp3 yang sudah ada di /mnt/data/
    for fname in os.listdir(data_path):
        if fname.endswith(".mp3"):
            audio_file = os.path.join(data_path, fname)
            break

# Pastikan file lagu berhasil ditemukan
if not audio_file or not os.path.exists(audio_file):
    print("Error: File lagu tidak ditemukan atau gagal diunggah!")
else:
    print(f"File lagu: {audio_file}")

    # 2. Putar lagu
    print("\nMemutar lagu...\n")
    display(Audio(filename=audio_file, autoplay=True))

    # 3. Fungsi efek mengetik untuk lirik lagu
    def animate_text(text, delay=0.05):
        """Menampilkan teks satu per satu dengan efek mengetik."""
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()  # Pindah ke baris baru

    # 4. Fungsi menampilkan lirik sesuai waktu lagu
    def sing_song():
        lyrics = [
            ("Kar'na kamu cantik", 2.0),
            ("'Kan kuberi s'galanya apa yang kupunya", 2.5),
            ("Dan hatimu baik", 2.0),
            ("Sempurnalah duniaku saat kau di sisiku", 2.5),
            ("Bukan kar'na make up di wajahmu", 2.0),
            ("Atau lipstik merah itu (di bibirmu)", 2.0),
            ("Lembut hati tutur kata", 1.5),
            ("Terciptalah cinta yang kupuja", 3.0),
            ("Tak peduli langit menertawakanku", 2.5),
            ("Kau mencuri mencuri hatiku, mimpiku, semua rinduku", 3.0),
            ("Kar'na kamu cantik", 2.0),
            ("'Kan kuberi s'galanya apa yang kupunya", 2.5),
            ("Dan hatimu baik", 2.0),
            ("Sempurnalah duniaku saat kau di sisiku", 2.5),
        ]

        print("\nMenampilkan lirik lagu...\n")
        for line, delay in lyrics:
            time.sleep(delay)  # Tunggu sesuai waktu dalam lagu
            animate_text(line, delay=0.05)

    # 5. Jalankan lirik sesuai lagu
    sing_song()
