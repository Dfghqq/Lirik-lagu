import os
import sys
import time
import requests
from IPython.display import Audio, display

# URL file MP3 dari GitHub (ganti dengan URL raw file MP3 kamu)
github_audio_url = "https://raw.githubusercontent.com/Dfghqq/Lirik-lagu/main/karena%20kamu%20cantik.mp3"
audio_file = "/mnt/data/karena_kamu_cantik.mp3"

# Buat folder jika belum ada
if not os.path.exists("/mnt/data/"):
    os.makedirs("/mnt/data/")

# Unduh file lagu jika belum ada
if not os.path.exists(audio_file):
    print("Mengunduh lagu dari GitHub...")
    response = requests.get(github_audio_url)
    with open(audio_file, "wb") as f:
        f.write(response.content)
    print("Unduhan selesai!")

# Pastikan file ada sebelum memutar
if os.path.exists(audio_file):
    print(f"File lagu: {audio_file}\n\nMemutar lagu...\n")
    display(Audio(filename=audio_file, autoplay=True))
else:
    print("Error: File lagu tidak ditemukan!")

# Fungsi efek mengetik untuk lirik lagu
def animate_text(text, delay=0.05):
    """Menampilkan teks satu per satu dengan efek mengetik."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Pindah ke baris baru

# Fungsi menampilkan lirik sesuai waktu lagu
def sing_song():
    lyrics = [
        ("Sempurnalah duniaku saat kau di sisiku", 2.5),
        ("Kar'na kamu cantik", 2.0),
        ("'Kan kuberi s'galanya apa yang kupunya", 2.0),
        ("Dan hatimu baik", 2.0),
        ("Sempurnalah duniaku saat kau di sisiku", 2.5),
        ("Bukan kar'na make up di wajahmu", 2.0),
        ("Atau lipstik merah itu (di bibirmu)", 2.0),
        ("Lembut hati tutur kata", 1.5),
        ("Terciptalah cinta yang kupuja", 3.0),
    ]

    print("\nMenampilkan lirik lagu...\n")
    for line, delay in lyrics:
        time.sleep(delay)  # Tunggu sesuai waktu dalam lagu
        animate_text(line, delay=0.05)

# Jalankan lirik sesuai lagu
sing_song()
