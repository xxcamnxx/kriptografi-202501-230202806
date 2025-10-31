# Laporan Praktikum Kriptografi
Minggu ke-: 5  
Topik: Cipher Klasik (Caesar, Vigenère, Transposisi) 
Nama: Exca Mutiara Nabilla

NIM: 230202806  
Kelas: 5 IKRA  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:

Menerapkan algoritma Caesar Cipher untuk enkripsi dan dekripsi teks.
Menerapkan algoritma Vigenère Cipher dengan variasi kunci.
Mengimplementasikan algoritma transposisi sederhana.
Menjelaskan kelemahan algoritma kriptografi klasik.    

---

## 2. Dasar Teori
##  Dasar Teori Cipher Klasik

Cipher klasik adalah metode enkripsi yang digunakan sebelum munculnya komputer dan kriptografi modern. Dasar teorinya sangat bergantung pada **substitusi (penggantian)** atau **transposisi (perubahan posisi)** karakter dalam *plaintext* (teks asli) untuk menghasilkan *ciphertext* (teks tersandi).


### 1. Cipher Substitusi

Dasar teori utama pada cipher substitusi adalah **mengganti setiap huruf** dari *plaintext* dengan huruf atau simbol lain, berdasarkan suatu kunci.

#### a. Caesar Cipher (Cipher Geser)
* **Dasar Teori:** Mengganti setiap huruf *plaintext* dengan huruf yang terletak pada **jumlah posisi yang tetap (kunci geseran)** di abjad.
* **Mekanisme:** Menggunakan aritmatika modular $(\text{mod } 26)$. Jika $ P $adalah nilai numerik huruf *plaintext* (A=0, B=1, dst.) dan$ K $ adalah kunci geser:
    $$\text{Enkripsi: } C = (P + K) \pmod{26}$$
    $$\text{Dekripsi: } P = (C - K) \pmod{26}$$
* **Kelemahan:** Hanya memiliki 25 kemungkinan kunci (sangat mudah dipecahkan dengan *brute force*).

#### b. Vigenère Cipher
* **Dasar Teori:** Menggunakan **kunci yang berupa kata** dan menerapkan Caesar Cipher yang berbeda untuk setiap huruf *plaintext* berdasarkan perulangan huruf-huruf kunci. Ini adalah bentuk **substitusi polialfabetik**.
* **Mekanisme:** Setiap huruf *plaintext* disubstitusikan menggunakan tabel Vigenère (atau *tabula recta*). Jika $P_i$ adalah huruf *plaintext* ke-i dan $K_i$ adalah huruf kunci ke-i (keduanya dinilai secara numerik):
    $$\text{Enkripsi: } C_i = (P_i + K_i) \pmod{26}$$
* **Kelebihan:** Jauh lebih kuat daripada Caesar karena menyembunyikan **frekuensi huruf** aslinya, yang merupakan titik lemah cipher monoalfabetik.

### 2. Cipher Transposisi

Dasar teori utama pada cipher transposisi adalah **mengubah urutan atau posisi** huruf-huruf *plaintext* tanpa mengubah huruf itu sendiri.

#### a. Transposisi Cipher (Misal: Columnar Transposition)
* **Dasar Teori:** Mengatur *plaintext* ke dalam sebuah **matriks (grid)** dengan lebar tertentu (ditentukan oleh kunci), lalu membaca urutan kolom yang berbeda untuk menghasilkan *ciphertext*.
* **Mekanisme:**
    1.  Tentukan **kunci** (misalnya, sebuah kata yang urutan hurufnya diindeks).
    2.  Tulis *plaintext* secara horizontal di bawah kunci.
    3.  Baca teks secara vertikal, mengikuti urutan numerik dari huruf-huruf kunci tersebut.
* **Kelebihan:** Sulit dipecahkan jika kunci panjang dan pengacakan (transposisi) dilakukan berulang-ulang, namun tetap rentan terhadap analisis frekuensi kata jika teksnya sangat panjang.

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Source Code

Implementasi Caesar Cipher
```def caesar_encrypt(plaintext, key):
    result = ""
    for char in plaintext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

def caesar_decrypt(ciphertext, key):
    return caesar_encrypt(ciphertext, -key)

# Contoh uji
msg = "CLASSIC CIPHER"
key = 3
enc = caesar_encrypt(msg, key)
dec = caesar_decrypt(enc, key)
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)
```
Implementasi Vigenère Cipher
```
def vigenere_encrypt(plaintext, key):
    result = []
    key = key.lower()
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            base = 65 if char.isupper() else 97
            result.append(chr((ord(char) - base + shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)
    return "".join(result)

def vigenere_decrypt(ciphertext, key):
    result = []
    key = key.lower()
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            base = 65 if char.isupper() else 97
            result.append(chr((ord(char) - base - shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)
    return "".join(result)

# Contoh uji
msg = "KRIPTOGRAFI"
key = "KEY"
enc = vigenere_encrypt(msg, key)
dec = vigenere_decrypt(enc, key)
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)

```
Implementasi Transposisi Sederhana
```
def transpose_encrypt(plaintext, key=5):
    ciphertext = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(plaintext):
            ciphertext[col] += plaintext[pointer]
            pointer += key
    return ''.join(ciphertext)

def transpose_decrypt(ciphertext, key=5):
    num_of_cols = int(len(ciphertext) / key + 0.9999)
    num_of_rows = key
    num_of_shaded_boxes = (num_of_cols * num_of_rows) - len(ciphertext)
    plaintext = [''] * num_of_cols
    col = 0
    row = 0
    for symbol in ciphertext:
        plaintext[col] += symbol
        col += 1
        if (col == num_of_cols) or (col == num_of_cols - 1 and row >= num_of_rows - num_of_shaded_boxes):
            col = 0
            row += 1
    return ''.join(plaintext)

# Contoh uji
msg = "TRANSPOSITIONCIPHER"
enc = transpose_encrypt(msg, key=5)
dec = transpose_decrypt(enc, key=5)
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)
```
---

## 5. Hasil dan Pembahasan


![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 6. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Apa kelemahan utama algoritma Caesar Cipher dan Vigenère Cipher?

   jawab : Cipher,Kelemahan Utama
a. Caesar Cipher,Kunci Terbatas. Hanya ada 25 kemungkinan kunci pergeseran. Sangat mudah dipecahkan menggunakan serangan brute force (mencoba semua kunci) atau analisis frekuensi sederhana.

b. Vigenère Cipher,"Periode Kunci yang Berulang. Kelemahannya terletak pada periode kunci (panjang kunci). Jika panjang kunci berhasil ditemukan (misalnya menggunakan metode Kasiski Test), cipher polialfabetik ini terdegradasi menjadi serangkaian Caesar Cipher yang dapat dipecahkan satu per satu."

- Mengapa cipher klasik mudah diserang dengan analisis frekuensi?
  jawab : Cipher klasik mudah diserang dengan analisis frekuensi karena setiap huruf terenkripsi memiliki pola kemunculan yang sama dengan huruf aslinya, sehingga distribusi frekuensi huruf dapat dibandingkan dengan bahasa alami.
  
- Bandingkan kelebihan dan kelemahan cipher substitusi vs transposisi.
  Jawab : Cipher substitusi:
Kelebihan: Mudah diterapkan dan cepat.
Kelemahan: Pola huruf tetap terlihat, mudah diserang analisis frekuensi.

Cipher transposisi:
Kelebihan: Menyembunyikan pola huruf dengan mengacak posisi.
Kelemahan: Tidak mengubah huruf asli, sehingga bisa rentan jika pola posisi terdeteksi.

)
---

## 7. Kesimpulan
Caesar Cipher, Vigenère Cipher, dan Transposisi Sederhana efektif untuk belajar dasar kriptografi, namun **tidak aman** untuk penggunaan modern karena mudah dipecahkan melalui analisis pola dan frekuensi.

---

## 8. Commit Log  
Contoh:
```
commit week5-cipher-klasik
Author: Exca mutiara nabilla <excaamn@gmail.com>
Date:   2025-10-31

  week5-cipher-klasik implementasi Cipher klasik dan laporan )
```
