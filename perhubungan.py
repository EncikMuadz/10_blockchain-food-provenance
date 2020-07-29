import threading

class Perhubungan(threading.Thread):
    ''' kelas ini mewakili tcp/ip soket perhubungan antara dua nodus, menyimpan soket pelanggan dan id nodus berhubung
    
        komunikasi terjadi melalui kelas ini
        mesej dihantar node berhubung disampaikan kepada node utama yg mencipta objek Perhubungan

        Instantiate objek baru, mula/start bebenang
            nodus_utama -> nodus penerima perhubungan
            soket -> soket pelanggan
            id -> id nodus terhubung
            perumah -> alamat ip nodus utama
            port -> port nodus utama
    '''
    def __init__(self, nodus_utama, soket, id, perumah, port):
        self.perumah = perumah
        self.port = port
        self.nodus_utama = nodus_utama
        self.soket = soket
        self.penamat_flag = threading.Event