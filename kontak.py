# berisi kelas kontak untuk menjalankan project program kontak

import dokumen
        
class Kontak:
    def __init__ (self):
        self.kontak = dokumen.membuka_kontak()

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
        dokumen.menyimpan_kontak(isi=self.kontak)