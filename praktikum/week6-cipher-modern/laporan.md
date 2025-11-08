# Laporan Praktikum Kriptografi
Minggu ke-: 6 
Topik: Cipher Modern (DES, AES, RSA)  
Nama: Exca Mutiara Nabilla  
NIM: 230202806 
Kelas: 5 IKRA 

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:

- Mengimplementasikan algoritma DES untuk blok data sederhana.
- Menerapkan algoritma AES dengan panjang kunci 128 bit.
- Menjelaskan proses pembangkitan kunci publik dan privat pada algoritma R
---

## 2. Dasar Teori
- DES (Data Encryption Standard) adalah algoritma simetris dengan kunci 56-bit yang bekerja pada blok 64-bit menggunakan struktur Feistel, namun kini dianggap tidak aman karena panjang kunci pendek.
- AES (Advanced Encryption Standard) juga simetris, menggunakan kunci 128/192/256-bit dengan struktur Substitution–Permutation Network, lebih cepat dan aman, menjadi standar enkripsi global saat ini.
- RSA (Rivest–Shamir–Adleman) merupakan algoritma asimetris yang menggunakan kunci publik dan privat, keamanannya bergantung pada kesulitan faktorisasi bilangan prima besar. RSA banyak digunakan untuk tanda tangan digital dan pertukaran kunci.

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan pip install pycryptodome

---

## 5. Source Code
1. Implementasi DES (Opsional, Simulasi)
```python
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

key = get_random_bytes(8)  # kunci 64 bit (8 byte)
cipher = DES.new(key, DES.MODE_ECB)

plaintext = b"ABCDEFGH"
ciphertext = cipher.encrypt(plaintext)
print("Ciphertext:", ciphertext)

decipher = DES.new(key, DES.MODE_ECB)
decrypted = decipher.decrypt(ciphertext)
print("Decrypted:", decrypted)
```
2. Implementasi AES-128
```python
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)  # 128 bit key
cipher = AES.new(key, AES.MODE_EAX)

plaintext = b"Modern Cipher AES Example"
ciphertext, tag = cipher.encrypt_and_digest(plaintext)

print("Ciphertext:", ciphertext)

# Dekripsi
cipher_dec = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
decrypted = cipher_dec.decrypt(ciphertext)
print("Decrypted:", decrypted.decode())
```
3. Implementasi RSA
```python
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Generate key pair
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

# Enkripsi dengan public key
cipher_rsa = PKCS1_OAEP.new(public_key)
plaintext = b"RSA Example"
ciphertext = cipher_rsa.encrypt(plaintext)
print("Ciphertext:", ciphertext)

# Dekripsi dengan private key
decipher_rsa = PKCS1_OAEP.new(private_key)
decrypted = decipher_rsa.decrypt(ciphertext)
print("Decrypted:", decrypted.decode())
```
)

---

## 6. Hasil dan Pembahasan
Hasil eksekusi program:
- DES berfungsi namun kurang aman untuk penggunaan modern.
- AES sangat aman dan efisien untuk enkripsi data.
- RSA cocok untuk enkripsi kunci dan autentikasi.

Secara keseluruhan, hasil uji menunjukkan setiap algoritma bekerja sesuai prinsipnya, dengan AES dan RSA lebih direkomendasikan untuk keamanan data modern dibanding DES.

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
(
1. Apa perbedaan mendasar antara DES, AES, dan RSA dalam hal kunci dan keamanan?

    Jawab :
 - DES menggunakan kunci simetris tunggal (56-bit) untuk enkripsi dan dekripsi; keamanannya lemah karena mudah diserang brute force.
 - AES juga simetris, tetapi memiliki kunci lebih panjang (128/192/256-bit) dan struktur lebih kompleks, sehingga jauh lebih aman dan efisien.
 - RSA bersifat asimetris, menggunakan sepasang kunci (publik dan privat); keamanannya bergantung pada kesulitan memfaktorkan bilangan prima besar.
   
2. Mengapa AES lebih banyak digunakan dibanding DES di era modern?
    Jawab : AES lebih digunakan karena lebih kuat, lebih cepat, dan lebih efisien. Panjang kuncinya yang besar membuatnya tahan terhadap serangan brute force, sedangkan DES dengan kunci 56-bit sudah dapat ditembus dalam waktu singkat oleh komputer modern.
3. Mengapa RSA dikategorikan sebagai algoritma asimetris, dan bagaimana proses pembangkitan kuncinya?
   Jawab : RSA disebut asimetris karena menggunakan dua kunci berbeda:
- Kunci publik untuk enkripsi (dapat dibagikan).
- Kunci privat untuk dekripsi (disimpan rahasia).

  Proses pembangkitan kunci RSA:
- Pilih dua bilangan prima besar 𝑝 dan 𝑞.
- Hitung 𝑛 = 𝑝 × 𝑞
- Hitung 𝜙 (𝑛) = (𝑝−1) ( 𝑞−1) ϕ(n)=(p−1)(q−1).
- Pilih bilangan 𝑒 yang relatif prima terhadap 𝜙 (𝑛).
- Hitung 𝑑 sebagai invers modulo 𝑒 terhadap 𝜙 (𝑛).

  **Kunci publik = (e, n), kunci privat = (d, n).**
)
---

## 8. Kesimpulan
DES, AES, dan RSA memiliki perbedaan mendasar pada jenis kunci dan tingkat keamanannya. DES dan AES termasuk algoritma simetris, sedangkan RSA adalah asimetris. DES kini sudah tidak aman karena panjang kuncinya pendek, sementara AES lebih unggul karena kunci panjang, struktur kompleks, dan efisiensi tinggi, sehingga menjadi standar enkripsi modern. RSA digunakan untuk pertukaran kunci dan keamanan komunikasi digital karena sistem dua kuncinya yang kuat dan berbasis pada kesulitan faktorisasi bilangan prima besar.

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit week6-cipher-modern
Author: Exca mutiara nabilla <excaamn@gmail.com>
Date:   2025-11-8

    week6-cipher-modern: Cipher Modern (DES, AES, RSA))
```
