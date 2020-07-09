""" Organisasi-organisasi yang boleh mengesahkan transaksi-transaksi yang berlaku didalam ekosistem
    TBD - Kelas objek organisasi untuk menambah organisasi
"""
class Organisasi:
    def __init__(self, orgId, nodeId, role):
        self.orgId = orgId
        self.nodeId = nodeId
        self.role = role