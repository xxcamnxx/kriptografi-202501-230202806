# Sejarah Kriptografi & Prinsip CIA

  kata Kriptografi berasal dar yunani yang berarti "tulisan rahasia" dimana ini merupakan teknik untuk mengenkripsi data yang dikirim supaya hanya dapat dimengerti oleh penerima yang dimaskud.
  
   Sejak zaman dahulu, pengiriman pesan rahasia telah menjadi hal umum dalam hampir setiap peradaban besar. Di era modern, kriptografi telah menjadi faktor utama dalam keamanan siber. Dimulai dengan melindungi pesan pribadi sehari-hari dan autentikasi tanda tangan digital sampai menjaga informasi pembayaran untuk belanja online serta melindungi data rahasia pemerintah dan komunikasi. Kriptografi memberikan perlindungan untuk privasi digital.
   
   Walaupun tradisi ini telah berlangsung selama ribuan tahun, pemanfaatan kriptografi dan area yang lebih luas dari kriptanalisis tetap dianggap cukup baru, dan baru saja mengalami kemajuan yang signifikan dalam satu abad terakhir. Seiring dengan penemuan komputasi modern di abad ke-19, permulaan era digital juga menandakan kelahiran kriptografi modern. Sebagai alat yang krusial untuk membangun kepercayaan digital, para matematikawan, ahli komputer, dan kriptografer mulai menciptakan metode kriptografi modern serta kriptosistem untuk melindungi data penting pengguna dari peretas, penjahat siber, dan pengintai.
   
 ** Kriptografi Kuno / klasik**
  100-44 SM: Untuk berbagi komunikasi yang aman di dalam tentara Romawi, Julius Caesar dihargai untuk penggunaan yang kemudian disebut Caesar Cipher, sebuah sandi substitusi di mana setiap huruf dari plaintext digantikan oleh huruf yang berbeda yang ditentukan dengan memindahkan sejumlah huruf maju atau mundur dalam alfabet Latin. Dalam kriptosistem kunci simetris ini, langkah dan arah spesifik transposisi huruf adalah kunci pribadi.
  
  **Vigenère Cipher**
  (abad ke-16): Menggunakan tabel alfabet untuk melakukan enkripsi dengan kunci berulang. Cipher ini dianggap sangat kuat dan dikenal sebagai “Cipher yang Tidak Dapat Dipecahkan” selama berabad-abad.
  
  
- Perkembangan **kriptografi modern** 
  1977: Ron Rivest, Adi Shamir, dan Leonard Adleman memperkenalkan kriptosistem kunci publik RSA, salah satu teknik enkripsi tertua untuk transmisi data yang aman yang masih digunakan hingga saat ini. Kunci publik RSA dibuat dengan mengalikan bilangan prima yang besar, yang sangat sulit bagi komputer yang paling kuat sekalipun untuk memfaktorkan tanpa pengetahuan sebelumnya tentang kunci privat yang digunakan untuk membuat kunci publik.

2001: Menanggapi kemajuan dalam daya komputasi, DES digantikan oleh algoritme enkripsi Advanced Encryption Standard (AES) yang lebih kuat. Serupa dengan DES, AES juga merupakan sebuah sistem kriptografi simetris, akan tetapi, ia menggunakan kunci enkripsi yang lebih panjang yang tidak dapat dipecahkan oleh perangkat keras modern.

- Evolusi menuju **kriptografi kontemporer**   
Blockchain dan Kriptografi (2008-sekarang): Bitcoin, yang diperkenalkan oleh Satoshi Nakamoto, memperkenalkan konsep blockchain, sebuah buku besar terdesentralisasi yang mengandalkan kriptografi untuk keamanan dan integritas data. Teknologi ini telah diperluas untuk berbagai aplikasi lain, termasuk kontrak pintar dan sistem keuangan terdesentralisasi (DeFi).

Sejarah kriptografi mencerminkan perkembangan yang berkelanjutan dalam menghadapi tantangan baru dan tuntutan untuk perlindungan informasi. Dari teknik dasar seperti Caesar Cipher hingga inovasi mutakhir seperti blockchain dan kriptografi kuantum, kriptografi telah menjadi elemen penting dalam dunia yang semakin terintegrasi dan digital saat ini

### Prinsip CIA
 CIA adalah konsep fundamental dalam keamanan siber yang terdiri dari tiga elemen utama, yaitu Confidentiality (Kerahasiaan), Integrity (Integritas), dan Availability (Ketersediaan). Setiap elemen dalam CIA akan menjadi bagian penting dari keamanan siber.
 a. Kerahasiaan (Confidentiality)
Aspek ini berkaitan dengan kebijakan dan teknologi yang diterapkan untuk menjaga informasi agar terhindar dari akses atau pengungkapan yang tidak sah. Dalam konteks privasi, data hanya boleh diakses oleh individu yang berwenang, sehingga data sensitif atau rahasia tetap terjaga dari pihak-pihak yang tidak diinginkan. contoh : Enkripsi melindungi informasi sensitif dari akses ilegal. Contoh: enkripsi end-to-end pada WhatsApp menjaga isi pesan hanya dapat dibaca pengirim dan penerima.

b. Integrity (Integritas)
Integritas berhubungan dengan keaslian dan kebenaran data. Dengan kata lain, informasi harus tetap konsisten dan tidak boleh mengalami perubahan yang tidak sah selama proses penyimpanan, pengiriman, atau pengolahan. Usaha untuk menjaga integritas informasi mencakup langkah-langkah guna mencegah perubahan atau manipulasi data yang tidak sah. contoh : Hash dan tanda tangan digital memastikan data tidak berubah. Contoh: Tanda tangan digital pada dokumen PDF.

c. Ketersediaan (Availability)
Ketersediaan mengindikasikan bahwa informasi perlu ada dan dapat diakses oleh pihak berwenang saat dibutuhkan. Artinya, sistem dan infrastruktur perlu dirancang serta dikelola sedemikian hingga mampu merespons permintaan akses informasi dengan cepat dan tanpa gangguan yang berarti.
Contoh : TLS/SSL pada situs perbankan mencegah serangan Man in the Middle agar layanan tetap aman diakses; OAuth memastikan hanya pengguna sah yang dapat masuk.




###  Quiz Singkat
Jawab pertanyaan berikut di laporan:  
1. Siapa tokoh yang dianggap sebagai bapak kriptografi modern?
   Claude shannon (1916–2001)
2. Sebutkan algoritma kunci publik yang populer digunakan saat ini.
  * RSA (Rivest–Shamir–Adleman) – paling banyak digunakan untuk enkripsi dan tanda tangan digital.
  *ECC (Elliptic Curve Cryptography) – lebih efisien dengan kunci lebih kecil.
  *Diffie-Hellman – digunakan untuk pertukaran kunci secara aman.
  *ElGamal – digunakan dalam sistem enkripsi dan tanda tangan digital.
3. Apa perbedaan utama antara kriptografi klasik dan kriptografi modern?
   Kriptografi klasik:
*Menggunakan teknik sederhana seperti substitusi dan transposisi.
*Biasanya hanya berbasis kunci simetris (satu kunci dipakai untuk enkripsi dan dekripsi).
Contoh: Caesar Cipher, Vigenère Cipher.

   Kriptografi modern:
*Berdasarkan teori matematika dan algoritma kompleks.
*Mendukung kunci publik (asimetri) selain kunci simetris.
*Digunakan dalam sistem komputer, internet, dan blockchain.
Contoh: AES (simetris), RSA & ECC (asimetri).



---

