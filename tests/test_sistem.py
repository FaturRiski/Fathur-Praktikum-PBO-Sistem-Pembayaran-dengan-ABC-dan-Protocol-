from datetime import datetime, timedelta

import pytest

from core.base import PaymentMethod, PembayaranGagal
from core.registry import buat_metode, daftar_plugin
from plugins import muat_semua_plugin
from plugins.virtual_account import VirtualAccount

muat_semua_plugin()


def test_abc_tidak_bisa_diinstansiasi():
    with pytest.raises(TypeError):
        PaymentMethod("uji")


def test_plugin_tak_dikenal_memunculkan_keyerror():
    with pytest.raises(KeyError):
        buat_metode("plugin-yang-tidak-ada")


def test_plugin_terdaftar():
    assert {"transfer", "ewallet", "qris", "va"} <= set(daftar_plugin())


def test_va_status_awal_menunggu():
    assert VirtualAccount().status == "menunggu"


def test_va_lunas_setelah_dibayar():
    va = VirtualAccount()
    va.proses(100_000)
    assert va.status == "lunas"


def test_va_ditolak_setelah_batas_waktu():
    sekarang = [datetime(2026, 11, 12, 10, 0)]
    va = VirtualAccount(batas_menit=60, jam=lambda: sekarang[0])
    sekarang[0] += timedelta(minutes=61)  # lewat batas waktu
    with pytest.raises(PembayaranGagal):
        va.proses(100_000)
    assert va.status == "kedaluwarsa"