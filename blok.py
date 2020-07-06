""" blok kelas
    tambah blok baharu
    mengsahihkan blok
    mendapatkan informasi blok terkini
"""
from collections import OrderedDict
from time import time
from maklumat import Maklumat

class Blok:
    # attributes
    def __init__(self, indeks, cincangan_sebelumnya, maklumat_maklumat, pembuktian, cetakan_masa):
        self.indeks = indeks
        self.cincangan_sebelumnya = cincangan_sebelumnya
        self.maklumat_maklumat = maklumat_maklumat
        self.pembuktian = pembuktian
        self.cetakan_masa = cetakan_masa
    
    # metode untuk menambah blok
    def penambah_blok(self):
        
        # gunapakai ordered list untuk karang blok baru
        blok = OrderedDict(
            [
                ('indeks', self.indeks),
                ('cincangan_sebelumnya', self.cincangan_sebelumnya),
                ('maklumat_maklumat', self.maklumat_maklumat),
                ('cetakan_masa', self.cetakan_masa),
                ('pembuktian', self.pembuktian)
            ]
        )
        return blok

    # penciptaan blok genesis
    def pemula_blok_genesis(self):
        self.penambah_blok

    # memanggil/memapar blok terkini
    def pemanggil_blok_terkini(self):
        pass