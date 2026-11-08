#Percobaan 1: Kontak Pembayaran dengan ABC

Pertanyaan Analisis (jawab di laporan)
1. Mengapa PaymentMethod("uji") gagal, padahal konstruktornya sudah benar?
= #(Karena PaymentMethod merupakan kelas abstrak yang memiliki method abstrak validasi() dan bayar(). Kelas abstrak tidak dapat dibuat objeknya secara langsung sebelum seluruh method abstraknya diimplementasikan.)

2. Apa yang terjadi pada Setengah dan mengapa pesan galatnya hanya menyebut bayar?
= (Kelas Setengah gagal diinstansiasi karena belum mengimplementasikan method bayar(). Pesan galat hanya menyebut bayar karena method validasi() sudah diimplementasikan.)

3. Mengapa proses() ditulis di kelas induk dan bukan di tiap subclass? Keuntungan apa yang didapat?
= Agar semua metode pembayaran memiliki urutan proses yang sama. Keuntungannya adalah kode lebih terstruktur, tidak terjadi pengulangan, dan setiap subclass cukup mengimplementasikan validasi serta pembayaran.

