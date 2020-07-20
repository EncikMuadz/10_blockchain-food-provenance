from collections import OrderedDict # gunapakai ordered dict(doubly linked list)

""" Kelas objek Maklumat/Transaksi
    organisasi bertanggungjawab akan mengemaskini perkembangan pada bahagian memasing
"""
class Maklumat:
    # attributes
    def __init__(self, organisasi_penambah, organisasi_penerima, perkembangan):
        self.organisasi_penambah = organisasi_penambah
        self.organisasi_penerima = organisasi_penerima
        self.perkembangan = perkembangan

    # paparkan maklumat daripada dictionary ke dalam bentuk string menggunakan __repr__
    def __repr__(self):
        return f'Organisasi Pengemaskini: {self.organisasi_penambah}, Organisasi Menerima: {self.organisasi_penerima}, Perkembangan: {self.perkembangan}'
        
    # mengarang maklumat baru untuk ditambah ke maklumat-maklumat semasa
    def penambah_maklumat(self):
        maklumat = OrderedDict(
            [
                ('organisasi_penambah', self.organisasi_penambah),
                ('organisasi_penerima', self.organisasi_penerima),
                ('perkembangan', self.perkembangan)
            ]
        )
        return maklumat