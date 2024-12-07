 #"Program Manajemen kontak"
import kontak

def main():

    kontak_kantor = kontak.Kontak()

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
            
if __name__ =="__main__":
    main()