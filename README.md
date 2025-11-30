# arkanoid-pawas

# Deskripsi
Proyek ini adalah implementasi dasar dari game arkade klasik Arkanoid (atau dikenal juga sebagai Breakout) yang dikembangkan menggunakan Python dan pustaka Pygame. Game ini berfokus pada mekanisme inti penghancuran balok dengan memantulkan bola menggunakan paddle yang dikontrol pemain.

Tujuan utama dari proyek ini adalah untuk melatih pemahaman dalam konsep pergerakan sprite, pendeteksian tabrakan (collision detection), dan logika kemenangan/kekalahan dalam lingkungan pengembangan game 2D.

# Fitur Utama
Game ini dirancang untuk menghadirkan pengalaman bermain single-player yang sederhana dan langsung:
Papan Pengendali (Paddle): Pemain mengontrol paddle secara horizontal untuk memantulkan bola ke atas.
Balok Sasaran (Bricks/Monsters): Susunan balok di bagian atas layar harus dihancurkan oleh pantulan bola.
Deteksi Tabrakan: Implementasi tabrakan yang responsif antara bola dengan paddle, dinding, dan setiap balok.
Pola Balok: Balok-balok diatur dalam tata letak awal yang terstruktur (misalnya, baris bertingkat).
Kondisi Kemenangan/Kekalahan:
Menang: Semua balok berhasil dihancurkan
Kalah: Bola jatuh melewati batas bawah layar
Sprite Kustom: Menggunakan kelas Picture untuk memuat gambar kustom (misalnya, ball.png, platform.png, enemy.png) dan menyediakan fallback jika gambar tidak ditemukan.

# Gerak Permainan
Panah kanan: gerak kanan
Panah kiri: gerak kiri

# Struktur dan Mekanisme
Logika game dibangun di sekitar beberapa kelas dan proses inti Pygame:
1. Kelas Dasar: Penggunaan kelas Area dan Picture sebagai sprite untuk menangani posisi, ukuran, dan penggambaran objek.
2. Pergerakan Bola: Bola bergerak dengan kecepatan konstan (bola_x, bola_y). Arah dibalik ketika terjadi tabrakan dengan dinding atau paddle.
3. Logika Penghancuran Balok: Fungsi utama terletak pada pengecekan m.rect.colliderect(ball.rect).
                              Jika terjadi tabrakan, balok dihapus dari daftar monster dan arah vertikal bola dibalik (bola_y *= -1).
4. Loop Utama: Mengelola semua masukan (input), memperbarui posisi objek, mengecek tabrakan, dan menggambar ulang layar dalam kecepatan frame rate 60 FPS.
