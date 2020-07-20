#program_masih_berjalan = True

#while program_masih_berjalan:

if __name__ == '__main__':
    while True:
        pilihan = input(
            '\nInteraksi dengan program paparan CLI\n\tTekan \'1\': Tambah Maklumat\n\tTekan \'2\': Tambah blok maklumat\n\tTekan \'q\': Keluar dari program'
        )
        if (pilihan == '1'):
            pass
        if (pilihan == '2'):
            pass
        if (pilihan == 'q'):
            exit() # keluar dari program secara kasar


# tidak menggunakan list comprehension 
    # [print('WIP') for i in range(0,1) if pilihan == '1']
    # [print('WIP') for i in range(0,1) if pilihan == '2']
    # [exit() for i in range(0,1) if pilihan == 'q']
