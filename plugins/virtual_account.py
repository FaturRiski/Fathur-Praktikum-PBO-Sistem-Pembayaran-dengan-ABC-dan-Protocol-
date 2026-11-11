from datetime import datetime, timedelta

from core.base import PaymentMethod
from core.registry import register_plugin
from core.utils import buat_id


@register_plugin("va")
class VirtualAccount(PaymentMethod):
    """Virtual Account: dibayar sebelum batas waktu, status awal 'menunggu'."""

    BATAS_TRANSAKSI = 10_000_000

    def __init__(self, bank: str = "BNI", batas_menit: int = 60, jam=datetime.now):
        super().__init__(f"Virtual Account {bank}")
        self._jam = jam  # fungsi pengambil waktu (bisa diganti saat pengujian)
        self.dibuat = self._jam()
        self.kedaluwarsa_pada = self.dibuat + timedelta(minutes=batas_menit)
        self.status = "menunggu"

    def cek_status(self) -> str:
        """Perbarui dan kembalikan status: menunggu, lunas, atau kedaluwarsa."""
        if self.status == "menunggu" and self._jam() > self.kedaluwarsa_pada:
            self.status = "kedaluwarsa"
        return self.status

    def biaya_admin(self, jumlah: float) -> float:
        return 4_000

    def validasi(self, jumlah: float) -> bool:
        return self.cek_status() == "menunggu" and jumlah <= self.BATAS_TRANSAKSI

    def bayar(self, jumlah: float) -> str:
        self.status = "lunas"
        return buat_id("VAC")