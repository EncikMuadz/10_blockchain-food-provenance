''' Implementasi program repl rantaian blok tanpa kelas'''

# kontainer untuk rantaian blok sesi ini
rantaian_data = []

def pemasuk_data():
    pengirim, penerima = input('\nMasukkan pengirim penerima dalam format berikut: Pengirim Penerima\n').split()
    mesej = input('\nTulis mesej anda:\n')
    rantaian_data.append((pengirim, penerima, mesej))

def antara_muka():
    program_berjalan = True
    while program_berjalan:
        pilihan_pengguna = input()
        if pilihan_pengguna == 'm':
            pemasuk_data()
        elif pilihan_pengguna == 'p':
            for elem in rantaian_data:
                print(elem)
        elif pilihan_pengguna == 'q':
            program_berjalan = False
        else:
            print('\nPilihan tidak sah!!!\n')

if __name__ == "__main__":
    antara_muka()