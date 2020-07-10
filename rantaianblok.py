""" Scaffold
    kelas objek rantaianblok
    attributes: senarai rantaian
    data-data semasa
"""
from maklumat import Maklumat
from blok import Blok
from time import time
class RantaianBlok:
    # attributes
    def __init__(self):
        self.rantaian = [] # mengandungi rantaian blok ditambah
        self.maklumat_maklumat_semasa = [] # maklumat-maklumat terkini untuk ditambah ke blok

    # menambah maklumat baharu
    def menambah_maklumat(self):
        id_organisasi = int(input())
        id_penerima = int(input())
        perkembangan = input()
        maklumat_baru = Maklumat(id_organisasi, id_penerima, perkembangan) # instantiate objek kelas maklumat
        self.maklumat_maklumat_semasa.append(maklumat_baru.penambah_maklumat()) # gabung ke list maklumat-maklumat semasa
        return self.maklumat_maklumat_semasa

    # menambah blok baharu
    def menambah_blok(self):
        cincangan_sebelumnya = int(input())
        pembuktian = input()
        cetakan_masa = time()
        blok_baharu = Blok(len(self.rantaian), cincangan_sebelumnya, self.maklumat_maklumat_semasa, pembuktian, cetakan_masa)
        self.rantaian.append(blok_baharu.penambah_blok())

    # mencincang blok data ke dalam bentuk cryptic
    def pencincang(self):
        pass

    # mendaftar organisasi yang berkepentingan
    def pendaftar_organisasi(self):
        pass

    # mengsahihkan rantaian blok
    def pengsahih_rantaian(self):
        pass

    # membuktikan kebenaran maklumat ditambah
    def pembukti(self):
        pass