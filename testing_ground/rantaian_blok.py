from hashlib import sha256

class Blok:
    ''' mewakili kelas nodus didalam LinkedList'''
    def __init__(self):
        self.data = None
        self.penerus = None

class Blockchain:
    ''' mewakili kelas LinkedList'''
    def __init__(self):
        self.kepala = None

mesej_awalan = 'Bacalah!!! dengan nama Tuhan mu..'

print(sha256(mesej_awalan.encode('UTF-8')).hexdigest())