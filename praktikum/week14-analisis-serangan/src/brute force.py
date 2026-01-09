import hashlib
import itertools
import string
import time

# ===== Konfigurasi target (simulasi) =====
password_asli = "ab1"  # password lemah & pendek
target_hash = hashlib.sha256(password_asli.encode()).hexdigest()

print("Target hash:", target_hash)

# ===== Parameter brute force =====
karakter = string.ascii_lowercase + string.digits  # a-z + 0-9
panjang_maks = 3

start = time.time()
percobaan = 0
ketemu = False

# ===== Proses brute force =====
for panjang in range(1, panjang_maks + 1):
    for kombinasi in itertools.product(karakter, repeat=panjang):
        tebakan = ''.join(kombinasi)
        hash_tebakan = hashlib.sha256(tebakan.encode()).hexdigest()
        percobaan += 1

        if hash_tebakan == target_hash:
            print("\nPassword ditemukan!")
            print("Password :", tebakan)
            print("Percobaan:", percobaan)
            ketemu = True
            break
    if ketemu:
        break

end = time.time()
print("Waktu eksekusi:", round(end - start, 3), "detik")
