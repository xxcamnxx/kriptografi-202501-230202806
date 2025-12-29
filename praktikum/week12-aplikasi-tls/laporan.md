# Laporan Praktikum Kriptografi
Minggu ke-: 12  
Topik: Aplikasi TLS & E-commerce
Nama: Exca Mutiara Nabilla  
NIM: 230202806
Kelas: 5IKRA  

---

## 1. Tujuan
- Menganalisis penggunaan kriptografi pada email dan SSL/TLS.
- Menjelaskan enkripsi dalam transaksi e-commerce.
- Mengevaluasi isu etika & privasi dalam penggunaan kriptografi di kehidupan sehari-hari.


---

## 2. Dasar Teori
Transport Layer Security (TLS) adalah protokol kriptografi yang mengamankan komunikasi data melalui kombinasi enkripsi simetris, kriptografi kunci publik, dan mekanisme autentikasi berbasis sertifikat digital. TLS menjamin kerahasiaan, integritas, dan autentikasi data dengan membentuk session key melalui proses handshake, sehingga pertukaran informasi berlangsung aman dari penyadapan dan manipulasi.

Dalam sistem e-commerce, TLS berperan krusial dalam melindungi data sensitif pengguna seperti kredensial akun dan informasi pembayaran. Implementasi TLS melalui HTTPS tidak hanya mencegah serangan man-in-the-middle, tetapi juga meningkatkan kepercayaan konsumen dan menjamin validitas transaksi, menjadikan TLS sebagai komponen fundamental keamanan dan keberlanjutan ekosistem perdagangan elektronik.

---

## 3. Hasil dan Pembahasan
Langkah 1 :
Website Shopee:
- Menggunakan HTTPS (TLS aktif)
- Sertifikat valid dan masih berlaku
- Diterbitkan oleh CA tepercaya
- Menggunakan algoritma kriptografi kuat (SHA-256, TLS)

  Langkah 2
  Bagaimana enkripsi digunakan untuk melindungi transaksi online?
  - Pada transaksi online seperti login dan pembayaran, enkripsi TLS melindungi data dengan mengamankan komunikasi antara browser pengguna dan server e-commerce. Saat login, username dan password dienkripsi menggunakan session key simetris (misalnya AES) yang dibentuk melalui proses TLS handshake. Pada tahap pembayaran, data sensitif seperti nomor kartu, CVV, dan detail transaksi juga dienkripsi sehingga hanya server tujuan yang dapat mendekripsi informasi tersebut, sementara pihak lain di jaringan tidak dapat membacanya.\

  Potensi ancaman jika TLS tidak digunakan
  - Tanpa TLS, data dikirim dalam bentuk plaintext sehingga sangat rentan terhadap ancaman keamanan. Salah satu serangan utama adalah Man-in-the-Middle (MITM), di mana penyerang dapat menyadap, mengubah, atau mencuri data pengguna saat transmisi berlangsung. Ancaman lain meliputi pencurian akun, pemalsuan transaksi, dan kebocoran data finansial, yang dapat merugikan pengguna serta menurunkan kepercayaan terhadap sistem e-commerce.

    Langkah 3
     Email terenkripsi seperti PGP dan S/MIME melindungi kerahasiaan isi pesan, namun isu privasi muncul pada pengelolaan kunci dan keterbukaan metadata email yang masih dapat dianalisis. Dari sisi etika, perusahaan dapat mendekripsi email karyawan untuk audit hanya jika dilakukan secara terbatas, transparan, dan berdasarkan kebijakan resmi, agar tidak melanggar hak privasi. Sementara itu, pengawasan pemerintah terhadap komunikasi terenkripsi harus menyeimbangkan keamanan dan privasi melalui regulasi yang jelas dan izin hukum, tanpa melemahkan sistem enkripsi secara keseluruhan.
---

## 4. Jawaban Pertanyaan
  
- Apa perbedaan utama antara HTTP dan HTTPS?
  Jawab : HTTP mengirimkan data tanpa enkripsi sehingga rentan disadap dan dimanipulasi, sedangkan HTTPS menggunakan protokol TLS untuk mengenkripsi komunikasi, menjamin kerahasiaan, integritas, dan autentikasi data.
- Mengapa sertifikat digital menjadi penting dalam komunikasi TLS?
  Jawab :Sertifikat digital berfungsi untuk memverifikasi identitas server dan mendistribusikan kunci publik secara aman. Dengan sertifikat yang diterbitkan oleh Certificate Authority (CA) tepercaya, pengguna dapat yakin bahwa mereka berkomunikasi dengan server yang sah dan bukan pihak palsu.
- Bagaimana kriptografi mendukung privasi dalam komunikasi digital, tetapi sekaligus menimbulkan tantangan hukum dan etika?
  Jawab: Kriptografi melindungi privasi komunikasi digital dengan mencegah akses tidak sah, namun juga menimbulkan tantangan hukum dan etika karena dapat membatasi pengawasan oleh perusahaan dan pemerintah. Hal ini memunculkan dilema antara perlindungan privasi individu dan kepentingan keamanan, audit, serta penegakan hukum.

---

## 5. Kesimpulan
Penggunaan HTTPS dengan TLS dan sertifikat digital sangat penting untuk menjamin keamanan komunikasi digital melalui enkripsi dan autentikasi. Kriptografi melindungi privasi dan kepercayaan pengguna, namun sekaligus menimbulkan tantangan hukum dan etika dalam menyeimbangkan kebutuhan keamanan, pengawasan, dan hak privasi individu.

---
