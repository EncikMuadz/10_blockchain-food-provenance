from hashlib import sha256

class Blok:
    ''' mewakili kelas nodus didalam LinkedList'''
    def __init__(self, data):
        self.data = data
        self.penerus = None # atau next element

# class Rantaian:
#     ''' mewakili kelas LinkedList'''
#     def __init__(self):
#         self.kepala = None
#     def attr_kep(self):
#         return self.kepala

mesej_awalan = 'Bacalah!!! dengan nama Tuhan mu..'
mesej_dicincang = str(sha256(mesej_awalan.encode('UTF-8')).hexdigest())
awalan = (mesej_awalan, mesej_dicincang)

ujian = Blok(data = awalan)
print(ujian.data)