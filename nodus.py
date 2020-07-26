import threading
import socket
from uuid import uuid4

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
        print(f'Bebenang kelas nodus dimulai pada, perumah: {self.perumah} dan port: {self.port}')

    def jalan(self):
        pass