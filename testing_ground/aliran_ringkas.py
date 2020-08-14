''' Implementasi program repl rantaian blok tanpa kelas'''

def antara_muka():
    while True:
        pilihan_pengguna = input()
        if pilihan_pengguna == 'm':
            print('\nMemasukkan data\n')
        elif pilihan_pengguna == 'q':
            return False
        else:
            print('\nPilihan tidak sah!!!\n')

if __name__ == "__main__":
    antara_muka()