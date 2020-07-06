from collections import OrderedDict # gunapakai ordered dict(doubly linked list)

""" Kelas objek Maklumat/Transaksi
    organisasi bertanggungjawab akan mengemaskini status pada bahagian memasing
"""
class Maklumat:
    # attributes
    def __init__(self, organisasi_penambah, organisasi_penerima, perkembangan):
        self.maklumat_maklumat_semasa = []
        self.organisasi_penambah = organisasi_penambah
        self.organisasi_penerima = organisasi_penerima
        self.perkembangan = perkembangan
        
    # mengarang maklumat baru untuk ditambah ke maklumat-maklumat semasa
    def penambah_maklumat(self):
        maklumat = OrderedDict(
            {
                ('organisasi_penambah', self.organisasi_penambah),
                ('organisasi_penerima', self.organisasi_penerima),
                ('perkembangan', self.perkembangan)
            }
        )
        self.maklumat_maklumat_semasa.append(maklumat)