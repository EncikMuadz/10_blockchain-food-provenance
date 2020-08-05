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
        self.penamat_flag = threading.Event
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
        self.soket.listen(2)

    def run(self):
        # jalinan perhubungan dengan peer lain
        while not self.penamat_flag.is_set():
            print('Menunggu jalinan perhubungan')
            hubungan, alamat = self.soket.accept()
            print(f'Menerima perhubungan daripada {alamat}')
            # pertukaran id antara nodus secara ringkas
            id_nodus_dihubung = hubungan.recv(4096).decode('utf-8') # terima id daripada nodus dihubung
            hubungan.send(self.id.encode('utf-8')) # hantar id kendiri kepada nodus dihubung

            # seterusnya adalah instantiate threads, dan memulakan bebenang hubungan
            
    def hubung(self, perumah, port):
        soket_hubung = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soket_hubung.connect((perumah, port))

        soket_hubung.send(self.id.encode('utf-8'))
        jalinan_id_diterima = soket_hubung.recv(4096).decode('utf-8')
        

# driver
nodus1 = Nodus('127.0.0.1', 8001)
nodus2 = Nodus('127.0.0.1', 8002)
time.sleep(2)
nodus1.hubung('127.0.0.1', 8002)
nodus2.hubung('127.0.0.1', 8001)
for nodus in [nodus1, nodus2]:
    print(f'Status {nodus} Alive?: {nodus.is_alive()}')