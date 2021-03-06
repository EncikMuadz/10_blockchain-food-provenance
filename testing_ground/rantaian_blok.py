from hashlib import sha256
from time import time
import json

class Blok:
    ''' mewakili kelas nodus didalam LinkedList'''
    def __init__(self, indeks, data_data, cetakan_masa, cincangan_sebelum):
        self.indeks = indeks # indeks blok ini
        self.data_data = data_data # data-data
        self.cetakan_masa = time() # masa berlaku
        self.cincangan_blok = self.pencincang_blok() # cincangan blok ini
        self.cincangan_sebelum = cincangan_sebelum # atau next element
    
    def pencincang_blok(self):
        string_blok = json.dumps(self.__dict__, sort_keys=True)
        return sha256(string_blok.encode('utf-8')).hexdigest()

class Rantaian:
    ''' mewakili kelas LinkedList'''
    def __init__(self):
        self.data_data_sesi = []
        self.rantaian_data = []
        self.kepala = Blok(0, self.data_data_sesi, time(), None)
    
    def pemula_kepala(self):
        self.rantaian_data.append(self.kepala)

    @property
    def pemeriksa_blok_terkini(self):
        return self.rantaian_data[-1]

    def penambah_blok(self, blok, bukti):
        cincangan_sebelum = self.pemeriksa_blok_terkini.hash

        if cincangan_sebelum != blok.cincangan_sebelum:
            return False
        blok.hash = bukti
        self.rantaian_data.append(blok)
        return True

    @staticmethod
    def pembukti_kerja(blok):
        cincangan_blok_dikira = blok.pencincang_blok()
        return cincangan_blok_dikira

    def penambah_data_baru(self, data):
        self.data_data_sesi.append(data)

    def pelombong(self):
        if not self.data_data_sesi:
            return False
        pemeriksa_blok_terkini = self.pemeriksa_blok_terkini
        blok_baharu = Blok(indeks=pemeriksa_blok_terkini.indeks, data_data=self.data_data_sesi, cetakan_masa=time(), cincangan_sebelum=pemeriksa_blok_terkini.cincangan_sebelum)
        bukti = self.pembukti_kerja(blok_baharu)
        self.penambah_blok(blok_baharu, bukti)
        return True

if __name__ == "__main__":
    ayat_awalan = 'Bacalah!!! dengan nama Tuhan mu..'