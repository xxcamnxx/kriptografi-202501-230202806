# Laporan Praktikum Kriptografi
Minggu ke-: 7  
Topik: Diffie-Hellman Key Exchange  
Nama: Exca Mutiara Nabilla  
NIM: 230202806  
Kelas: 5 IKRA  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:

Melakukan simulasi protokol Diffie-Hellman untuk pertukaran kunci publik.
Menjelaskan mekanisme pertukaran kunci rahasia menggunakan bilangan prima dan logaritma diskrit.
Menganalisis potensi serangan pada protokol Diffie-Hellman (termasuk serangan Man-in-the-Middle / MITM).


---

## 2. Dasar Teori
Diffie-Hellman Key Exchange adalah salah satu metode kriptografi kunci publik yang digunakan untuk menukar kunci rahasia secara aman melalui jaringan yang tidak aman. Teknik ini memungkinkan dua pihak (misalnya Alice dan Bob) yang sebelumnya tidak memiliki kunci bersama untuk menghasilkan kunci enkripsi yang sama tanpa perlu mengirimkan kunci tersebut secara langsung.
Keamanan Diffie-Hellman bergantung pada sulitnya Discrete Logarithm Problem, yaitu menghitung nilai 
𝑎 dari persamaan 𝐴 = 𝑔^𝑎 mod 𝑝
Tanpa mengetahui kunci privat, sangat sulit bagi penyadap untuk mendapatkan kunci rahasia.

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

```
)

---

## 5. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 6. Jawaban Pertanyaan
1. Mengapa Diffie-Hellman memungkinkan pertukaran kunci di saluran publik?
Jawab : Karena Diffie-Hellman memungkinkan dua pihak membuat kunci rahasia yang sama tanpa pernah mengirimkan kunci tersebut secara langsung melalui jaringan.
Yang dipertukarkan di saluran publik hanyalah:
- bilangan publik 𝑝1 𝑔
- kunci publik masing-masing pihak (misalnya 𝑔𝑎 mod 𝑝 dan 𝑔𝑏 mod 𝑝)
Walaupun orang lain dapat melihat nilai itu, mereka tetap tidak dapat menemukan kunci rahasia bersama, karena memecahkan kunci membutuhkan memecahkan Discrete Logarithm Problem, yang sangat sulit secara matematis.

2. Apa kelemahan utama protokol Diffie-Hellman murni?
Jawab :Tidak ada autentikasi (tidak memverifikasi identitas pihak lain)

3. Bagaimana cara mencegah serangan MITM pada protokol ini?
Jawab : MITM dapat dicegah dengan menambahkan mekanisme autentikasi, misalnya:
Menggabungkan DH dengan:
- Tanda tangan digital
  Pihak yang mengirim kunci publik menandatanganinya, sehingga penerima bisa memverifikasi bahwa kunci benar-benar berasal dari pihak tersebut.
- Sertifikat digital dan PKI (misalnya pada HTTPS/TLS)
  Kunci publik divalidasi menggunakan sertifikat dari otoritas terpercaya.
- Pre-Shared Key (PSK)
  Kedua pihak sudah berbagi kata sandi sebelumnya untuk memverifikasi identitas.
- Variasi yang sudah mendukung autentikasi, seperti:
  Authenticated Diffie-Hellman
  ECDHE + sertifikat pada TLS
---

## 7. Kesimpulan
Diffie-Hellman merupakan metode pertukaran kunci dalam kriptografi modern yang memungkinkan dua pihak menghasilkan kunci rahasia bersama secara aman meskipun berkomunikasi melalui saluran publik. Keamanan metode ini bergantung pada kesulitan memecahkan Discrete Logarithm Problem, sehingga pihak ketiga tidak dapat dengan mudah menebak kunci rahasia meski mengetahui parameter publik yang dipertukarkan.

Namun, protokol Diffie-Hellman murni memiliki kelemahan utama, yaitu tidak adanya mekanisme autentikasi sehingga rentan terhadap serangan Man-In-The-Middle (MITM). Oleh karena itu, dalam penerapan nyata, protokol ini umumnya dikombinasikan dengan teknik autentikasi tambahan seperti tanda tangan digital, sertifikat digital, atau mekanisme keamanan lain agar komunikasi menjadi aman dan terjamin keasliannya.

Secara keseluruhan, Diffie-Hellman adalah fondasi penting dalam banyak protokol keamanan modern dan menjadi salah satu solusi utama dalam pertukaran kunci secara aman di jaringan terbuka.

---

## 8. Commit Log
```
commit week7-diffie-hellman
Author: Exca
Date:   2025-11-19

    week7-diffie-hellman: implementasi Diffie-Hellman Key Exchange dan laporan )
```
