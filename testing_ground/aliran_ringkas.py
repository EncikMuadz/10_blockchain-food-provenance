''' Implementasi program repl rantaian blok tanpa kelas'''

from hashlib import sha256

# kontainer untuk rantaian blok sesi ini
rantaian_data = []
data_data = []

def pemasuk_data():
    pengirim, penerima = input('\nMasukkan pengirim penerima dalam format berikut: Pengirim Penerima\n').split()
    mesej = input('\nTulis mesej anda:\n')
    data_data.append((pengirim, penerima, mesej))

def penghad_masukan_data():
    if len(data_data) > 3:
        print('\nCincang data terlebih dahulu\n')
        raise Exception('\nMesej perlu dicincang dahulu sebelum mesej baru dihantar\n')

def pencincang_data(data_data):
    string_data_data = ''.join([str(elem) for elem in data_data[:3]])
    cincangan = sha256(string_data_data.encode('utf-8')).hexdigest()
    rantaian_data.append([string_data_data, cincangan])

def pengosong_kontainer(data_data):
    '''set kembali data_data kepada tiada'''
    for elem in data_data:
        data_data.remove(elem)

def antara_muka():
    program_berjalan = True
    while program_berjalan:
        pilihan_pengguna = input()
        if pilihan_pengguna == 'm':
            penghad_masukan_data()
            pemasuk_data()
        elif pilihan_pengguna == 'p':
            for elem in data_data:
                print(elem)
        elif pilihan_pengguna == 'c':
            pencincang_data(data_data)
            pengosong_kontainer(data_data)
        elif pilihan_pengguna == 'rb':
            for elem in rantaian_data:
                print(elem)
        elif pilihan_pengguna == 'q':
            program_berjalan = False
        else:
            print('\nPilihan tidak sah!!!\n')

if __name__ == "__main__":
    antara_muka()