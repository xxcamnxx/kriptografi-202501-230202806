# Laporan Praktikum Kriptografi
Minggu ke-: 11  
Topik: Secret Sharing (Shamir’s Secret Sharing) 
Nama: Exca Mutiara Nabilla  
NIM: 230202806
Kelas: 5IKRA

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:  
1. Menjelaskan konsep **Shamir Secret Sharing** (SSS).  
2. Melakukan simulasi pembagian rahasia ke beberapa pihak menggunakan skema SSS.  
3. Menganalisis keamanan skema distribusi rahasia.  

---

## 2. Dasar Teori
Secret Sharing, khususnya Shamir’s Secret Sharing (SSS), adalah metode kriptografi untuk membagi sebuah rahasia (secret) menjadi beberapa bagian (shares) yang didistribusikan ke sejumlah pihak. Rahasia hanya dapat direkonstruksi jika jumlah share yang dikumpulkan memenuhi batas minimum tertentu (threshold). Tujuannya adalah meningkatkan keamanan dan keandalan penyimpanan data, karena tidak ada satu pihak pun yang memegang rahasia secara utuh.

Shamir’s Secret Sharing bekerja berdasarkan konsep interpolasi polinomial dalam matematika. Rahasia disimpan sebagai konstanta dalam suatu polinomial derajat (k−1), kemudian beberapa titik pada polinomial tersebut dibagikan sebagai share. Selama jumlah share yang dikumpulkan kurang dari threshold, rahasia tidak dapat diketahui. Namun, jika minimal k share tersedia, polinomial dapat direkonstruksi dan rahasia diperoleh kembali.

Skema ini banyak digunakan dalam sistem keamanan modern seperti manajemen kunci kriptografi, backup data terdistribusi, dan keamanan sistem blockchain. Keunggulan utama Shamir’s Secret Sharing adalah sifatnya yang aman secara informasi (information-theoretic security), artinya rahasia tetap sepenuhnya aman meskipun penyerang memiliki sebagian share yang tidak mencukupi.

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
from secretsharing import SecretSharer

# Rahasia yang ingin dibagi
secret = "KriptografiUPB2025"

# Bagi menjadi 5 shares, ambang batas 3 (minimal 3 shares untuk rekonstruksi)
shares = SecretSharer.split_secret(secret, 3, 5)
print("Shares:", shares)

# Rekonstruksi rahasia dari 3 shares
recovered = SecretSharer.recover_secret(shares[:3])
print("Recovered secret:", recovered)
```
)

---

## 5. Hasil dan Pembahasan
Hasil eksekusi program 

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 6. Jawaban Pertanyaan
1. Keuntungan utama Shamir’s Secret Sharing (SSS) dibandingkan membagikan salinan kunci secara langsung adalah keamanan yang lebih tinggi. Pada pembagian salinan kunci, jika satu salinan bocor maka seluruh sistem langsung terancam. Sedangkan pada SSS, satu atau beberapa share tidak cukup untuk mengetahui rahasia, sehingga kebocoran sebagian data tidak menyebabkan kunci utama terungkap.

2. Peran threshold (k) adalah menentukan jumlah minimum share yang harus dikumpulkan untuk merekonstruksi rahasia. Threshold ini menjadi kontrol utama keamanan: semakin besar nilai k, semakin sulit bagi pihak tidak berwenang untuk mendapatkan rahasia. Selama jumlah share yang dimiliki kurang dari k, informasi tentang rahasia tetap tidak dapat diperoleh.

3. Contoh skenario nyata penggunaan SSS adalah pada manajemen kunci perusahaan atau organisasi. Misalnya, kunci utama server hanya bisa diakses jika minimal 3 dari 5 administrator hadir dan menggabungkan share mereka. Dengan cara ini, tidak ada satu admin pun yang bisa menyalahgunakan kunci secara sepihak, sekaligus mencegah kehilangan akses jika satu admin tidak tersedia.
---

## 7. Kesimpulan
Shamir’s Secret Sharing merupakan metode kriptografi yang efektif untuk melindungi rahasia dengan cara membaginya ke dalam beberapa bagian tanpa mengorbankan keamanan. Dengan mekanisme threshold, sistem tetap aman meskipun sebagian share bocor, dan rahasia hanya dapat diakses melalui kerja sama pihak yang berwenang. Oleh karena itu, SSS sangat cocok diterapkan pada sistem yang membutuhkan keamanan tinggi, keandalan, dan kontrol akses bersama, seperti manajemen kunci dan sistem terdistribusi.

---

## 8. Commit Log

Contoh:
```
commit week11
Author: Exca Mutiara nabilla <excaamn@gmail.com>
Date:   2025-12-20

    week11-secret-sharing : implementasi secret sharing dan laporan 
```
