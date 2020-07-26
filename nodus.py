import threading
import socket
from uuid import uuid4
import time

class Nodus(threading.Thread):
    ''' Kelas ini blueprint kepada objek nodus
    
        ip -> alamat ip/ host ip
        port -> port dibuka
    '''
    def __init__(self, perumah, port):
        threading.Thread.__init__(self)
        self.perumah = perumah
        self.port = port
        self.id = str(uuid4().hex)
        self.soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.pemula()
        print(f'Bebenang kelas nodus dimulai pada, perumah: {self.perumah} dan port: {self.port}\n')

    def pemula(self):
        print(f'Mengikat/Bind nodus pada {self.perumah}:{self.port}\n')
        self.soket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # guna balik alamat dan port
        self.soket.bind((self.perumah, self.port)) # ikat soket pada alamat perumah dan port
        self.soket.settimeout(5.0)
        self.soket.listen(1)
        print('Memulai bebenang\n')
        self.start()
        print('Sertakan/Join bebenang dengan bebenang utama\n')
        self.join()

    def jalan(self):
        pass

# driver
nodus1 = Nodus('127.0.0.1', 8001)
nodus2 = Nodus('127.0.0.1', 8002)
time.sleep(2)
for nodus in [nodus1, nodus2]:
    print(f'Status {nodus} Alive?: {nodus.is_alive()}')