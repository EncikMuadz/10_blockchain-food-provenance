""" blok kelas
    tambah blok baharu
    mengsahihkan blok
    mendapatkan informasi blok terkini
"""
from time import time
from maklumat import Maklumat
from hashlib import sha256

class Blok:
    # attributes
    def __init__(self, indeks, cincangan_sebelumnya, maklumat_maklumat, pembuktian, cetakan_masa):
        self.indeks = indeks
        self.cincangan_sebelumnya = cincangan_sebelumnya
        self.maklumat_maklumat = maklumat_maklumat
        self.pembuktian = pembuktian
        self.cetakan_masa = time()

    # # paparkan maklumat daripada dictionary ke dalam bentuk string menggunakan __repr__
    # def __repr__(self):
    #     return 'Indeks: {}, Cincangan Lepas: {}, Maklumat-maklumat: {}, Pembuktian: {}, Cetakan Masa: {}'.format(self.indeks, self.cincangan_sebelumnya, self.maklumat_maklumat, self.pembuktian, self.cetakan_masa)
    
    # mencincang blok data ke dalam bentuk cryptic dan dapatkan cincangan blok terkini
    def pencincang_blok(self):
        jalinan_blok = f'{self.indeks}{self.cincangan_sebelumnya}{self.maklumat_maklumat}{self.pembuktian}{self.cetakan_masa}'
        return sha256(jalinan_blok.encode()).hexdigest()
    # memanggil/memapar blok terkini
    def pemanggil_blok_terkini(self):
        pass