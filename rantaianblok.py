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
        # super(RantaianBlok, self).__init__() # pewarisan attribute daripada kelas Blok
        self.rantaian = [] # mengandungi rantaian blok ditambah
        self.maklumat_maklumat_semasa = [] # maklumat-maklumat terkini untuk ditambah ke blok

    # menambah maklumat baharu
    def penambah_maklumat(self, organisasi_penambah, organisasi_penerima, perkembangan):
        maklumat_baru = Maklumat(organisasi_penambah, organisasi_penerima, perkembangan) # instantiate objek kelas maklumat
        self.maklumat_maklumat_semasa.append(maklumat_baru.penambah_maklumat()) # gabung ke list maklumat-maklumat semasa
        return self.maklumat_maklumat_semasa

    # metode untuk menambah blok
    def penambah_blok(self, pembuktian, cincangan_sebelumnya):
        
        # gunapakai ordered list untuk karang blok baru
        blok = Blok(
            indeks = len(self.rantaian),
            cincangan_sebelumnya = cincangan_sebelumnya,
            maklumat_maklumat = self.maklumat_maklumat_semasa,
            cetakan_masa = self.cetakan_masa,
            pembuktian = pembuktian
        )

        self.maklumat_maklumat_semasa = [] # tetapkan kembali ke list tanpa elemen-elemen
        self.rantaian.append(blok) # append blok baru ke rantaian
        return blok

    # penciptaan blok genesis
    def pemula_blok_genesis(self):
        self.penambah_blok(pembuktian=0, cincangan_sebelumnya=0)

    # mendaftar organisasi yang berkepentingan
    def pendaftar_organisasi(self):
        pass

    # mengsahihkan rantaian blok
    def pengsahih_rantaian(self):
        pass

    # membuktikan kebenaran maklumat ditambah
    def pembukti(self):
        pass