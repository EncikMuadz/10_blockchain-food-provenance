''' Implementasi program repl rantaian blok tanpa kelas'''

from hashlib import sha256 # untuk mencincang data
from collections import deque # untuk blockchain
from datetime import datetime

rantaian_data = deque() # kontainer untuk rantaian blok sesi ini
rantaian_data_cincangan = deque() # kontainer untuk cincangan data sesi ini
rantaian_data_cetakanmasa_blok = deque() # kontainer untuk cetakan masa sesi ini
data_data = []

def pemula():
    print('\nSelamat Datang\n')
    mesej_awalan = tuple(input('\nMasukkan kata-kata/mesej sebelum memulakan sesi:\n '))
    pencincang_data((mesej_awalan))
    antara_muka()

def pemasuk_data():
    pengirim, penerima = input('\nMasukkan pengirim penerima dalam format berikut: Pengirim Penerima\n').split()
    mesej = input('\nTulis mesej anda:\n')
    data_data.append((pengirim, penerima, mesej))

def penghad_masukan_data():
    if len(data_data) > 3:
        print('\nCincang data terlebih dahulu\n')
        raise Exception('\nMesej perlu dicincang dahulu sebelum mesej baru dihantar\n')

def pencincang_data(data_data):
    try:
        string_data_data = ''.join([str(elem) for elem in data_data])
        cincangan = sha256(string_data_data.encode('utf-8')).hexdigest()
    except ValueError:
        raise Exception('\nTiada mesej-mesej untuk dicincang\n')


    # dua deque satu untuk blok maklumat, satu untuk cincangan
    rantaian_data.append(string_data_data)
    rantaian_data_cincangan.append(cincangan)

    # letak cetakan masa ke dalam senarai rantaian data
    pencetak_masa()

def pencetak_masa():
    sekarang = datetime.now()
    cetakan_masa = datetime.timestamp(sekarang)
    rantaian_data_cetakanmasa_blok.append(cetakan_masa)

def pengosong_kontainer(data_data):
    '''set kembali data_data kepada tiada'''
    for elem in data_data:
        data_data.remove(elem)

def antara_muka_pendahuluan():
    print('\nPilih \'m\' untuk memasukkan data\nPilih \'dd\' untuk memaparkan data-data sedia ada\nPilih \'c\' untuk cincang data-data\nPilih \'rb\' untuk memaparkan rantaian blok sedia ada\nPilih \'q\' untuk keluar\n')

def antara_muka():
    program_berjalan = True
    while program_berjalan:
        antara_muka_pendahuluan()
        pilihan_pengguna = input('\nSila buat pilihan: \n')
        if pilihan_pengguna == 'm':
            penghad_masukan_data()
            pemasuk_data()
        elif pilihan_pengguna == 'dd':
            for elem in data_data:
                print(elem)
        elif pilihan_pengguna == 'c':
            pencincang_data(data_data)
            pengosong_kontainer(data_data)
        elif pilihan_pengguna == 'rb':
            for elem, elem_cincang, elem_cetakan in zip(rantaian_data, rantaian_data_cincangan, rantaian_data_cetakanmasa_blok):
                print(elem, elem_cincang, elem_cetakan)
        elif pilihan_pengguna == 'q':
            program_berjalan = False
        else:
            print('\nPilihan tidak sah!!!\n')

if __name__ == "__main__":
    pemula()