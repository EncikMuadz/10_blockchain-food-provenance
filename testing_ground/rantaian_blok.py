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

if __name__ == "__main__":
    ayat_awalan = 'Bacalah!!! dengan nama Tuhan mu..'