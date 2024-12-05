 #"Program Manajemen kontak"
def membuka_kontak(path='kontak.txt'):
    with open(path, mode='r') as file:
        kontak = file.readlines()
    return kontak

def menyimpan_kontak(path='kontak.txt', isi=[]):
    with open(path, mode='w') as file:
        file.writelines(isi)
        
class Kontak:
    def __init__ (self):
        self.kontak = membuka_kontak()

    def melihat_kontak(self):
        # melihat semua kontak
        if self.kontak:
            for num, item in enumerate(self.kontak, start=1):
                print(f'{num}. ' + item)
        else:
            print("kontak masih kosong")
            return 1

    def menambah_kontak(self):
        nama = input("Masukan nama kontak yang baru: ")
        HP = input("Masukan nomor kontak yang baru: ")
        email = input("Masukan email kontak yang baru: ")
        kontak_baru = f'{nama} ({HP}, {email})' + '\n'
        self.kontak.append(kontak_baru)
        print("Kontak baru berhasil di tambahkan")

    def menghapus_kontak(self):
        # menghapus kontak
        if self.melihat_kontak() == 1:
            return
        else:
            try:
                i_hapus = int(input("Masukan nomor kontak yang mau di hapus: "))
                del self.kontak[i_hapus - 1]
                print("Kontak berhasil di hapus")
            except:
                print("anda memasukan pilihan yang salah, masukan angka,bukan abjad atau karakter lain")
            
    def keluar_kontak(self):
        menyimpan_kontak(isi=self.kontak)

kontak_kantor = Kontak()

while True:
    print("\nMenu Kontak")
    print("1. Melihat Semua Kontak")
    print("2. Menambahkan Kontak Baru")
    print("3. Menghapus Kontak")
    print("4. Keluar Dari Kontak")

    pilihan = input("Masukkan pilihan menu kontak (1,2,3 atau 4): ")

    if pilihan == '1':
        kontak_kantor.melihat_kontak()

    elif pilihan == '2':
        kontak_kantor.menambah_kontak()

    elif pilihan == '3':
        kontak_kantor.menghapus_kontak()

    elif pilihan == '4':
        # keluar dari kontak
        kontak_kantor.keluar_kontak()
        break
    else:
        print("Maaf,nomor yang anda masukan tidak ada di menu kontak")

