from hashlib import sha256
from time import time
import json

class Blok:
    ''' mewakili kelas nodus didalam LinkedList'''
    def __init__(self, indeks, data_data, cetakan_masa, cincangan_sebelum):
        self.indeks = indeks
        self.data_data = data_data
        self.cetakan_masa = time() 
        self.cincangan_sebelum = cincangan_sebelum # atau next element
    
    def pencincang_blok(self):
        string_blok = json.dumps(self.__dict__, sort_keys=True)
        return sha256(string_blok.encode('utf-8')).hexdigest()

# class Rantaian:
#     ''' mewakili kelas LinkedList'''
#     def __init__(self):
#         self.kepala = None
#     def attr_kep(self):
#         return self.kepala

if __name__ == "__main__":
    ayat_awalan = 'Bacalah!!! dengan nama Tuhan mu..'