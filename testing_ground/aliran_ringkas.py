''' Implementasi program repl rantaian blok tanpa kelas'''

# kontainer untuk rantaian blok sesi ini
rantaian_data = []

def pemasuk_data(pengirim, penerima, mesej):
    pengirim, penerima = input('\nMasukkan pengirim penerima dalam format berikut: Pengirim Penerima\n').split()
    mesej = input('\nTulis mesej anda:\n')
    return pengirim, penerima, mesej

def antara_muka():
    while True:
        pilihan_pengguna = input()
        if pilihan_pengguna == 'm':
            pemasuk_data()
        elif pilihan_pengguna == 'q':
            return False
        else:
            print('\nPilihan tidak sah!!!\n')

if __name__ == "__main__":
    antara_muka()