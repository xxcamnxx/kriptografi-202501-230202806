# Laporan Praktikum Kriptografi
Minggu ke-: 3  
Topik: Modular Math (Aritmetika Modular, GCD, Bilangan Prima, Logaritma Diskrit)  
Nama: Exca Mutiara Nabilla  
NIM: 230202806  
Kelas: 5IKRA  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:

Menyelesaikan operasi aritmetika modular.
Menentukan bilangan prima dan menghitung GCD (Greatest Common Divisor).
Menerapkan logaritma diskrit sederhana dalam simulasi kriptografi.

---

## 2. Dasar Teori
Dalam kriptografi, aritmatika modular secara langsung mendukung sistem kunci publik seperti RSA dan Diffie–Hellman , dan menyediakan medan hingga yang mendasari kurva eliptik , dan digunakan dalam berbagai algoritma kunci simetris termasuk Advanced Encryption Standard (AES), International Data Encryption Algorithm (IDEA), dan RC4 . RSA dan Diffie–Hellman menggunakan eksponensiasi modular .
Aritmetika modular adalah sistem aritmetika di mana bilangan "berputar kembali" setelah mencapai nilai tertentu yang disebut modulus (n). Artinya, kita hanya memperhatikan sisa hasil bagi dari suatu pembagian.

Peran dalam Kriptografi
- Digunakan dalam RSA, Diffie–Hellman, dan Elliptic Curve Cryptography (ECC).
- Menjamin hasil operasi besar tetap dalam ruang bilangan terbatas.
- Dasar perhitungan untuk enkripsi, dekripsi, tanda tangan digital, dan verifikasi.

Aritmetika modular adalah dasar matematika penting dalam kriptografi modern.Ia memungkinkan perhitungan yang efisien, menjaga keamanan dengan modulus besar, dan menjadi kunci dalam pembentukan serta penggunaan kunci publik–privat pada sistem enkripsi.

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Source Code

1. Aritmatika modular
```python
 def mod_add(a, b, n): return (a + b) % n
 def mod_sub(a, b, n): return (a - b) % n
 def mod_mul(a, b, n): return (a * b) % n
 def mod_exp(base, exp, n): return pow(base, exp, n)  # eksponensiasi modular

 print("7 + 5 mod 12 =", mod_add(7, 5, 12))
 print("7 * 5 mod 12 =", mod_mul(7, 5, 12))
 print("7^128 mod 13 =", mod_exp(7, 128, 13))
```
2. GCD & Algoritma Euclidean
```python
  def gcd(a, b):
     while b != 0:
         a, b = b, a % b
     return a

 print("gcd(54, 24) =", gcd(54, 24))
```
3. Extended Euclidean Algorithm
 ```python
   def egcd(a, b):
 if a == 0:
     return b, 0, 1
 g, x1, y1 = egcd(b % a, a)
 return g, y1 - (b // a) * x1, x1

 def modinv(a, n):
     g, x, _ = egcd(a, n)
     if g != 1:
         return None
     return x % n

 print("Invers 3 mod 11 =", modinv(3, 11))  # hasil: 4
```
4. Logaritma Diskrit
```python
   def discrete_log(a, b, n):
     for x in range(n):
         if pow(a, x, n) == b:
             return x
     return None

 print("3^x ≡ 4 (mod 7), x =", discrete_log(3, 4, 7))  # hasil: 4
```    

---

## 5. Hasil dan Pembahasan
Kode pertama menunjukkan bagaimana operasi dasar seperti penjumlahan, perkalian, dan perpangkatan dapat dilakukan secara efisien dalam sistem modular. Proses ini menjadi dasar dari mekanisme enkripsi dan dekripsi pada algoritma seperti RSA.

Selanjutnya, kode GCD dan invers modular memiliki peran penting dalam memastikan keterkaitan antarbilangan. GCD digunakan untuk memeriksa apakah dua bilangan bersifat relatif prima, sedangkan invers modular memungkinkan proses pembalikan dari enkripsi ke dekripsi pada sistem kunci publik. Tanpa adanya invers modular, pesan terenkripsi tidak dapat dikembalikan ke bentuk aslinya.

Terakhir, kode logaritma diskrit menggambarkan tingkat kesulitan dalam mencari nilai eksponen 
𝑥 dari persamaan 𝑎 𝑥 ≡ 𝑏 ( mod 𝑛) a x ≡b(modn). Kompleksitas inilah yang menjadi dasar keamanan algoritma seperti Diffie–Hellman.

Secara keseluruhan, keempat kode tersebut menunjukkan keterkaitan erat antara konsep matematika dasar dengan penerapannya dalam melindungi keamanan data digital melalui kriptografi.

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 6. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  

- Apa peran aritmetika modular dalam kriptografi modern?
  jawab : Aritmetika modular adalah tulang punggung kriptografi modern karena memungkinkan operasi matematis:
a. Terbatas dalam ruang bilangan aman (finite field)
b. Dapat dibalik hanya dengan kunci tertentu
c. Efisien untuk komputasi besar
d. Dan sulit dipecahkan secara matematis tanpa kunci

- Mengapa invers modular penting dalam algoritma kunci publik (misalnya RSA)?
  Jawab : karena invers modular adalah kunci utama yang membuat algoritma kriptografi seperti RSA bisa mengenkripsi dan mendekripsi dengan aman.
  
- Apa tantangan utama dalam menyelesaikan logaritma diskrit untuk modulus besar?
  Jawab : Tantangan utama dalam menyelesaikan logaritma diskrit untuk modulus besar adalah tidak adanya algoritma efisien yang dapat menghitung eksponen 
𝑥 dalam persamaan 𝑎𝑥 ≡ 𝑏(mod 𝑛) a x ≡b(modn) — menjadikannya dasar keamanan banyak algoritma kriptografi modern.
)
---

## 7. Kesimpulan
Aritmetika Modular adalah sistem perhitungan berbasis sisa hasil bagi, di mana operasi dilakukan “dalam lingkaran” nilai tertentu (modulus).
→ Digunakan untuk menjaga agar hasil operasi tetap dalam ruang bilangan terbatas dan efisien untuk komputasi besar.
GCD (Greatest Common Divisor) berperan dalam menentukan apakah dua bilangan relatif prima — syarat penting agar invers modular dapat dihitung.
→ Dihitung menggunakan Algoritma Euclidean, yang juga melibatkan operasi modulus.
Dalam kriptografi modern, kedua konsep ini menjadi fondasi utama:
Aritmetika modular memungkinkan operasi enkripsi dan dekripsi berbasis pangkat modulo (misalnya pada RSA dan Diffie–Hellman).
GCD digunakan untuk memilih kunci publik yang valid serta menghitung invers modular.
Invers modular adalah penghubung antara kunci publik dan kunci privat (misalnya 
𝑒 dan 𝑑 dalam RSA), memastikan bahwa pesan yang dienkripsi dapat dikembalikan ke bentuk aslinya dengan benar.
Tantangan utama logaritma diskrit pada modulus besar adalah tidak adanya algoritma efisien untuk membalik operasi pangkat modulo, sehingga masalah ini sangat sulit diselesaikan — dan justru menjadi dasar keamanan sistem kriptografi seperti RSA, Diffie–Hellman, dan ECC.


---

## 8. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Exca Mutiara Nabilla <excaamn@gmail.com>
Date:   2025-09-20

    week3-modmath: implementasi dan laporan )
```
