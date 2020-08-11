from hashlib import sha256

class Blok:
    ''' mewakili kelas nodus didalam LinkedList'''
    def __init__(self, data, penerus = None):
        self.data = data
        self.penerus = penerus # atau next element

# class Rantaian:
#     ''' mewakili kelas LinkedList'''
#     def __init__(self):
#         self.kepala = None
#     def attr_kep(self):
#         return self.kepala

ayat_awalan = 'Bacalah!!! dengan nama Tuhan mu..'
ayat_dicincang = str(sha256(ayat_awalan.encode('UTF-8')).hexdigest())
awalan = (ayat_awalan, ayat_dicincang)
ujian = Blok(data = awalan)
print(ujian.data)

ayat_kedua = 'yang menciptakan..'
ayat_dicincang2 = str(sha256(ayat_kedua.encode('UTF-8')).hexdigest())
kedua = (ayat_kedua, ayat_dicincang2)
ujian2 = Blok(data = kedua)
ujian.penerus(ayat_dicincang)