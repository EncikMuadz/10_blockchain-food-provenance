""" Scaffold
    kelas objek rantaianblok
    attributes: senarai rantaian
    data-data semasa
"""
from collections import OrderedDict
from maklumat import Maklumat
from blok import Blok
from time import time

class RantaianBlok(Blok):
    # attributes
    def __init__(self):
        super(RantaianBlok, self).__init__()
        self.rantaian = [] # mengandungi rantaian blok ditambah
        self.maklumat_maklumat_semasa = [] # maklumat-maklumat terkini untuk ditambah ke blok

    # menambah maklumat baharu
    def penambah_maklumat(self):
        id_organisasi = int(input())
        id_penerima = int(input())
        perkembangan = input()
        maklumat_baru = Maklumat(id_organisasi, id_penerima, perkembangan) # instantiate objek kelas maklumat
        self.maklumat_maklumat_semasa.append(maklumat_baru.penambah_maklumat()) # gabung ke list maklumat-maklumat semasa
        return self.maklumat_maklumat_semasa

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
        self.penambah_blok()

    # mendaftar organisasi yang berkepentingan
    def pendaftar_organisasi(self):
        pass

    # mengsahihkan rantaian blok
    def pengsahih_rantaian(self):
        pass

    # membuktikan kebenaran maklumat ditambah
    def pembukti(self):
        pass