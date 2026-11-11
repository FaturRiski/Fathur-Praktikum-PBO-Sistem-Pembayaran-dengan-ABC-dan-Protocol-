#Percobaan 1: Kontak Pembayaran dengan ABC

Pertanyaan Analisis (jawab di laporan)
1. Mengapa PaymentMethod("uji") gagal, padahal konstruktornya sudah benar?
= #(Karena PaymentMethod merupakan kelas abstrak yang memiliki method abstrak validasi() dan bayar(). Kelas abstrak tidak dapat dibuat objeknya secara langsung sebelum seluruh method abstraknya diimplementasikan.)

2. Apa yang terjadi pada Setengah dan mengapa pesan galatnya hanya menyebut bayar?
= (Kelas Setengah gagal diinstansiasi karena belum mengimplementasikan method bayar(). Pesan galat hanya menyebut bayar karena method validasi() sudah diimplementasikan.)

3. Mengapa proses() ditulis di kelas induk dan bukan di tiap subclass? Keuntungan apa yang didapat?
= Agar semua metode pembayaran memiliki urutan proses yang sama. Keuntungannya adalah kode lebih terstruktur, tidak terjadi pengulangan, dan setiap subclass cukup mengimplementasikan validasi serta pembayaran.

#Percobaan 2: Kontrak notifikasi dengan protocol
1.Mengapa EmailNotifer dianggap Notifier padahal tidak mewarisinya?
= Karena EmailNotifier memiliki method kirim() sesuai dengan struktur yang ditentukan oleh Protocol Notifier. Protocol menggunakan structural subtyping sehingga tidak membutuhkan pewarisan secara langsung

2. Apa yang terjadi saat @runtime_checkable dihapus? Mengapa Python mewajibkannya untuk isinstance()?
= Program akan menghasilkan TypeError ketika menggunakan isinstance(). Karena dekorator @runtime_checkable diperlukan agar Protocol dapat diperiksa kesesuaiannya saat program berjalan

3. Jika kirim() pada WhatsAppNotifier diubah menjadi kirim(self), apakah isinstance() tetap bernilai True? Jelaskan.
= Ya, kemungkinan tetap bernilai True karena pemeriksaan runtime hanya mengecek keberadaan nama method, bukan jumlah parameter atau tipe argumennya.

#Percobaan 3: Merangkai PaymentProcessor

1.	Bagian mana pada checkout() yang membuktikan pemroses tidak bergantung pada metode pembayaran tertentu?
= Bagian metode.proses(jumlah) membuktikan bahwa PaymentProcessor hanya menggunakan kontrak PaymentMethod tanpa bergantung pada kelas pembayaran tertentu seperti TransferBank atau EWallet.
2.	Pembayaran GoPay Rp150.000 ditolak. Apa penyebabnya, dan di method mana penolakan itu diputuskan?
= Karena saldo GoPay hanya Rp100.000, sedangkan pembayaran sebesar Rp150.000. Penolakan diputuskan pada method validasi() di kelas EWallet.
3.	Mengapa PaymentProcessor cukup meminta Notifier (Protocol) dan bukan sebuah kelas dasar notifikasi (ABC)? Apa untungnya bagi kode yang ditulis pihak lain?
= Karena Protocol memungkinkan objek yang memiliki method kirim() digunakan tanpa harus mewarisi kelas tertentu. Keuntungannya, kode dari pihak lain dapat langsung digunakan selama memenuhi kontrak yang ditentukan.

#Percobaan 4: Sistem Plugin dengan registry
1.	Apa yang terjadi bila dekorator @register_plugin("ewallet") dihapus dari ewallet.py? Mengapa?
= Plugin EWallet tidak akan terdaftar di registry sehingga tidak dapat ditemukan ketika dipanggil menggunakan buat_metode(). Akibatnya, program menghasilkan KeyError.
2.	Mengapa muat_semua_plugin() perlu dipanggil sebelum buat_metode()?
= Karena fungsi tersebut mengimpor seluruh modul plugin agar dekorator pendaftaran dijalankan dan setiap plugin masuk ke registry.
3.	Jelaskan bagaimana rancangan ini menerapkan prinsip Open/Closed.
= Sistem dapat dikembangkan dengan menambahkan plugin baru tanpa mengubah kode inti seperti PaymentProcessor dan main.py. Dengan demikian, sistem terbuka untuk penambahan tetapi tertutup untuk perubahan kode yang sudah ada.

#Tugas 1: Plugin QRIS

#Tugas 2: TelegramNotifer tanpa pewarisan
