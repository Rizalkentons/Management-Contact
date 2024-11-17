 #"Program Manajemen kontak"

kontak1 = {'nama' : "Rizal" , 'hp' : '293123190' , 'email' : 'Rizalkentons@AI.com'}
kontak2 = {'nama' : "Boren" , 'hp' : '299898310' , 'email' : 'boreninja@AI.com'}
kontak3 = {'nama' : "Burjo" , 'hp' : '299898310' , 'email' : 'burjoninja@AI.com'}
kontak = [kontak1, kontak2, kontak3]

while True:
    print("\nMenu Kontak")
    print("1. Melihat  Semua Kontak")
    print("2. Menambahkan Kontak Baru")
    print("3. Menghapus Kontak")
    print("4. Keluar Dari Kontak")

    pilihan = input("Masukkan pilihan menu kontak (1,2,3 atau 4): ")

    if pilihan == '1':
        #melihat semua kontak
        if kontak :
            for num, item in enumerate(kontak , start=1):
                print(f'\n{num}. {item["nama"]} ({item["hp"]} , {item["email"]})')
        else:
            print("kontak masih kosong")

    elif pilihan == '2':
        #menambahkan kontak
        nama = input("Masukan nama kontak yang baru: ")
        hp = input("Masukan nomor kontak yang baru: ")
        email = input("Masukan email kontak yang baru: ")
        kontak_baru = {'nama':nama, 'hp':hp, 'email':email}
        kontak.append(kontak_baru)
        print("Kontak baru berhasil di tambahkan")

    elif pilihan == '3':
        #menghapus kontak
        if kontak:
            for num, item in enumerate(kontak, start=1):
                print(f'\n{num}. {item["nama"]} ({item["hp"]} , {item["email"]})')
        else:
            print("kontak masih kosong")
            continue
        i_hapus = int(input("Masukan nomor kontak yang mau di hapus: "))
        del kontak[i_hapus - 1]
        print("\nKontak berhasil di hapus")
    elif pilihan == '4':
        #keluar dari kontak
        break
    else:
        print("Maaf,nomor yang anda masukan tidak ada di menu kontak")