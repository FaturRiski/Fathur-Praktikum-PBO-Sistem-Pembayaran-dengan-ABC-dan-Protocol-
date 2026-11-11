from core.processor import PaymentProcessor


class NotifierRusak:
    """kirim() salah tanda tangan: tidak menerima penerima dan pesan."""

    def kirim(self) -> None:
        print("terkirim")


# Saat dijalankan, isinstance() lolos karena nama method 'kirim' ada.
# Hanya mypy yang menandai baris ini sebagai galat tipe.
pemroses = PaymentProcessor(NotifierRusak())
print("objek PaymentProcessor berhasil dibuat (runtime tidak protes)")