import threading

class Perhubungan(threading.Thread):
    ''' kelas ini mewakili tcp/ip soket perhubungan antara dua nodus, menyimpan soket pelanggan dan id nodus berhubung
    
        komunikasi terjadi melalui kelas ini
        mesej dihantar node berhubung disampaika kepada node utama yg mencipta objek Perhubungan

        Instantiate objek baru, mula/start bebenang
            nodus_utama -> nodus penerima perhubungan
            soket -> soket pelanggan
            id -> id nodus terhubung
            perumah -> alamat ip nodus utama
            port -> port nodus utama
    '''