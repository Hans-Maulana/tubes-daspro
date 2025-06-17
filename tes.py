# File : <namafile..py >
# Penulis : <2472024, 2472052, 2472064>
# Manajemen LACCE Coffeshop
# Kamus Data Main
# stop : variabel boolean
# pilihan : variabel penyimpan hasil return dari fungsi yang dipanggil
# flag : variabel boolean 
# hasil : variabel penyimpan hasil return dari fungsi yang dipanggil (arr)
# admin : variabel penyimpan variabel hasil dari indeks ke 0 (int)

def aturKode():
    global kupon
    print()
    print("="*100)
    print("📦  PENGATURAN KODE PROMO".center(100))
    print("="*100)
    
    print()
    print("🎟️  Kode Promo Tersedia:")
    kosong = True
    for i in range(len(kupon)):
        if kupon[i][0] != "TIDAK JADI": 
            if kupon[i][0] is not None :
                print(f"  🔹 {kupon[i][0]}   -   Potongan: {kupon[i][1]*100:.0f}%")
                kosong = False
    if kosong:
        print("  (Belum ada kode promo yang tersedia)")
    print()
    print("1️⃣  Tambah Kode Promo")
    print("2️⃣  Hapus Kode Promo")
    print("3️⃣  🔙 Kembali ke Halaman Utama")

    pilihan = input("\n📌 Pilih Menu [1/2/3]: ")
    while pilihan not in ["1", "2", "3"]:
        print("⚠️  Input tidak valid. Coba lagi.")
        pilihan = input("📌 Pilih Menu [1/2/3]: ")

    # Menambah kode promo
    if pilihan == "1":
        while True:
            promo = input("\n🆕 Masukkan Kode Promo Baru: ").upper()
            potongan = input("💸 Masukkan Potongan (dalam persen, contoh 10): ")
            while not potongan.isdigit():
                print("⚠️  Potongan harus berupa angka.")
                potongan = input("💸 Masukkan Potongan (contoh 10): ")
            potongan_baru = int(potongan) / 100

            sudah_ada = False
            for i in range(len(kupon)):
                if kupon[i][0] is not None and promo == kupon[i][0].upper():
                    sudah_ada = True
                    break
            if sudah_ada:
                print("⚠️  Kode promo sudah tersedia. Coba lagi.")
            else:
                kupon.append([promo, potongan_baru])
                print(f"✅ Kode promo '{promo}' berhasil ditambahkan!")
                break

   
    elif pilihan == "2":
        if kosong:
            print()
            print("⚠️  Tidak ada kode promo yang bisa dihapus.")
            return
        while True:
            print()
            promo = input("❌ Masukkan Kode Promo yang ingin dihapus: ").upper()
            ditemukan = False
            for i in range(len(kupon)):
                if kupon[i] is not None and promo == kupon[i][0].upper():
                    ditemukan = True
                    break
            if not ditemukan:
                print("⚠️  Kode promo tidak ditemukan. Coba lagi.")
            else:
                konfirmasi = input(f"🔐 Yakin ingin menghapus '{promo}'? [ya/tidak]: ").lower()
                while konfirmasi not in ["ya", "tidak"]:
                    print("⚠️  Input salah!")
                    konfirmasi = input("🔐 Yakin ingin menghapus? [ya/tidak]: ").lower()
                if konfirmasi == "ya":
                    kupon[i][0] = None
                    kupon[i][1] = None
                    print(f"🗑️  Kode promo '{promo}' berhasil dihapus.")
                else:
                    print("❎  Penghapusan dibatalkan.")
                break
    else:
        print()
        print("🔙 Kembali ke halaman utama...")          

# Kamus Data Lokal
# user : variabel input username pendafataran akun (str)
# pw : variabel input password pendaftaran akun (str)
# Fungsi ini berguna untuk pendaftaran akun baru.
def signup():
    global username, password
    print()
    print("="*100)
    print(f"📋  SELAMAT DATANG DI MENU SIGN UP  📋 ".center(100))
    print("="*100)

    user = str(input("🔹 Buat Username : "))
    pw = str(input("🔒 Buat Password : "))

    if user in username:
        print()
        print("🚫 Username tidak tersedia, silakan coba lagi.")
        signup()
    else:
        username.append(user)
        password.append(pw)
        order.append([])
        riwayat.append([])
        pay.append([])
        allpay.append([])
        subtotal.append(0)
        pendapatan.append([0, 0, 0])
        poin.append([user, 0])
        print()
        print("✅ Berhasil mendaftar! Selamat datang,", user)
        print("-"*100)
    return True

# Kamus Data Lokal
# user : variabel input username login akun (str)
# pw : variabel input password login akun (str)
# mark : variabel boolean
# flag : variabel boolean
# i : variabel pengendali loop untuk counter indeks array
# Fungsi ini berguna untuk login akun yang telah terdaftar.
def login():
    global username, password, layer
    print()
    print("="*100)
    print("🔐  LOGIN - MASUK KE AKUN ANDA".center(100))
    print("="*100)
    mark = False
    while not mark :
        user = str(input("👤 Username : "))
        pw = str(input("🔑 Password : "))

        if user == username[0] and pw == password[0]:
            flag = True
            print()
            print("✅ Login sebagai Admin berhasil!")
            mark = True
            i = 0
        else:
            for i in range(len(username)):
                if user == username[i] and pw == password[i]:
                    flag = False
                    mark = True
                    break
                else:
                    mark = False
            if not mark:
                print()
                print("❌ Username atau Password salah! Coba lagi.")
                print()
            else:
                print()
                print("✅ Login Berhasil! Selamat datang,", user)
    arr = [flag, i]
    layer = 2
    return arr

# Kamus Data Lokal
# admin, i_user : variabel parameter
# pilihan : variabel input pilihan kategori (str)
# kategori : variabel kategori menu (str)
# minuman : variabel input jenis minuman (str)
# nama : variabel input nama menu baru (str)
# harga : variabel input harga menu baru (str)
# ulang : variabel input tambah menu lagi (str)
# Fungsi ini berguna untuk user admin dalam menambah menu baru.
def tambahMenu(admin, i_user):
    global menu, layer
    while True:
        print()
        print("="*100)
        print(f"➕  TAMBAH MENU BARU".center(100))
        print("="*100)
        print("1️⃣  Makanan")
        print("2️⃣  Minuman")
        print("3️⃣  Dessert")
        print("4️⃣  🔙 Kembali ke Home")
        print()
        pilihan = str(input("📌 Pilih kategori menu (1-4): "))

        if pilihan == "1":
            kategori = "makanan"
        elif pilihan == "2":
            print()
            print("☕ Jenis Minuman:")
            print("   1. Coffee")
            print("   2. Non-Coffee")
            minuman = str(input("   Jenis Minuman (1/2): "))
            while minuman not in ["1", "2"]:
                print("   ⚠️  Input tidak valid. Coba lagi.")
                minuman = str(input("   Pilih (1/2): "))
            kategori = "coffee" if minuman == "1" else "noncoffee"
        elif pilihan == "3":
            kategori = "dessert"
        elif pilihan == "4":
            print()
            print("🔙 Kembali ke Home...")
            print()
            layer = 2
            break
        else:
            print()
            print("⚠️ Pilihan tidak valid. Silakan coba lagi.")
            continue
        print()
        nama = input("📝 Nama Menu : ")
        harga = input("💰 Harga (Rp): ")
        while not harga.isdigit():
            print("   ⚠️ Harga harus berupa angka.")
            harga = input("💰 Harga (Rp): ")
        harga = int(harga)
        
        menu.append([kategori, nama, harga])
        print()
        print(f"✅ Menu *{nama}* berhasil ditambahkan ke kategori *{kategori.upper()}* dengan harga Rp{harga:,}")
        print()
        ulang = input("🔁 Tambah menu lagi? [ya] | [tidak] : ").lower()
        if ulang != 'ya':
            print()
            print("🔚 Selesai menambahkan menu.")
            layer = 2
            break

# Kamus Data Lokal
# diskon : variabel total diskon (int)
# i : variabel pengendali loop
# j : variabel pengendali loop
# Fungsi ini berguna untuk user admin dalam menghitung total pendapatan
def hitungTotal():
    global riwayat, allpay, total, subtotal, layer, pendapatan
    print()
    print("-"*100)
    print("📊  REKAP HASIL PENDAPATAN".center(100))
    print("-"*100)

    diskon = 0

    for i in range(1, len(riwayat)):  
        print()
        print(f"👤 Username : {username[i]}")
        print("-" * 100)
        if not riwayat[i]:
            print("💴 Belum ada Transaksi")
        else:
            print(f"{'🍽️  Nama Barang':<25} {'💵 Harga'}")
            for j in range(len(riwayat[i])):
                print(f"   {riwayat[i][j]:<22} Rp. {allpay[i][j]:,}")
                total += allpay[i][j]
            print()
            print(f"🎁 Total Diskon     : Rp. {pendapatan[i][1]:,.0f}")
            print(f"🧾 Total Pembayaran : Rp. {pendapatan[i][2]:,.0f}")
            print("-" * 100)
            diskon += pendapatan[i][1]
            print()
            print(F"💼 TOTAL PENDAPATAN BERSIH : Rp. {total - diskon:,.0f}")
            
    print("-"*100)
    layer = 2

# Kamus Data Lokal
# admin, i_user : variabel parameter
# pilihan : variabel input pilihan menu (str)
# i : variabel pengendali loop
# found : variabel boolean
# nama_menu : variabel input nama menu yang harganya akan diubah (str)
# harga_input : variabel input harga baru dari menu yang diinput (str)
# harga_baru : variabel yang menyimpan harga baru dari menu yang dipilih (int)
# ulang : variabel input ubah harga menu lain (str)
# Fungsi ini berguna untuk user admin dalam mengubah harga suatu menu.
def ubahHarga(admin, i_user):
    global menu, layer
    while True:
        print()
        print("="*100)
        print("💵  UBAH HARGA MENU".center(100))
        print("="*100)
        print("1️⃣  Minuman")
        print("2️⃣  Makanan")
        print("3️⃣  Dessert")
        print("4️⃣  🔙 Kembali ke Home")
        print()
        pilihan = input("📌 Pilihan Anda (1-4): ")
        if pilihan == "1":
            print()
            print("☕ Menu Coffee:")
            for i in range(len(menu)):
                if "noncoffee" in menu[i]:
                    print(f" - {menu[i][1]:<20} Rp. {menu[i][2]:,}")
            print()
            print("🥤 Menu Non-Coffee:")
            for i in range(len(menu)):
                if "coffee" in menu[i]:
                    print(f" - {menu[i][1]:<20} Rp. {menu[i][2]:,}")
        elif pilihan == "2":
            print()
            print("🍽️  Menu Makanan:")
            for i in range(len(menu)):
                if "makanan" in menu[i]:
                    print(f" - {menu[i][1]:<100} Rp. {menu[i][2]:,}")
        elif pilihan == "3":
            print()
            print("🍰 Menu Dessert:")
            for i in range(len(menu)):
                if "dessert" in menu[i]:
                    print(f" - {menu[i][1]:<30} Rp. {menu[i][2]:,}")
        elif pilihan == "4":
            print()
            print("🔙 Kembali ke Home...")
            print()
            layer = 2
            break
        else:
            print()
            print("⚠️ Input tidak valid. Silakan coba lagi.")
            continue

        
        found = False
        while not found:
            print()
            nama_menu = input("📝 Masukkan nama menu yang ingin diubah: ")
            for i in range(len(menu)):
                if nama_menu.lower() == menu[i][1].lower():
                    print(f"🔧 Menu ditemukan: {menu[i][1]} (Harga saat ini: Rp. {menu[i][2]:,})")
                    found = True
                    break
            if not found:
                print("❌ Menu tidak ditemukan. Coba lagi.")

        
        harga_input = input("💰 Masukkan harga baru: ")
        while not harga_input.isdigit():
            print("⚠️ Harga harus berupa angka.")
            harga_input = input("💰 Masukkan harga baru: ")
        harga_baru = int(harga_input)

        menu[i][2] = harga_baru
        print(f"✅ Harga menu '{menu[i][1]}' berhasil diubah menjadi Rp. {harga_baru:,}")
        print()
        ulang = input("🔁 Ingin ubah harga menu lain? [ya/tidak]: ").lower()
        if ulang != "ya":
            print()
            print("🏠 Kembali ke halaman utama...")
            layer = 2
            break

# Kamus Data Lokal
# i_user : variabel parameter
# flag : variabel boolean
# pilihan : variabel input pilihan menu (str)
# i : variabel pengendali loop
# Fungsi ini berguna untuk menampilkan menu menu sesuai kategori.
def printMenu(i_user):
    global menu
    if not order[i_user]:
        flag = True
    else :
        flag = False
    print()
    print("="*100)
    print("🍴 PILIH KATEGORI MENU".center(100))
    print("="*100)
    print("1️⃣  Minuman")
    print("2️⃣  Makanan")
    print("3️⃣  Dessert")
    if flag:
        print("4️⃣  🔙 Kembali ke halaman utama")
    print()
    pilihan = input("📌 Pilihan: ")

    if pilihan == "1":
        print()
        print("🥤 NON-COFFEE:")
        for i in range(len(menu)):
            if "noncoffee" in menu[i]:
                print(f" - {menu[i][1]:<40} Rp. {menu[i][2]:,}")
        print()
        print("☕ COFFEE:")
        for i in range(len(menu)):
            if "coffee" in menu[i]:
                print(f"- {menu[i][1]:<40} Rp. {menu[i][2]:,}")
    elif pilihan == "2":
        print()
        print("🍽️  MAKANAN:")
        for i in range(len(menu)):
            if "makanan" in menu[i]:
                print(f" - {menu[i][1]:<40} Rp. {menu[i][2]:,}")
    elif pilihan == "3":
        print()
        print("🍰 DESSERT:")
        for i in range(len(menu)):
            if "dessert" in menu[i]:
                print(f" - {menu[i][1]:<40} Rp. {menu[i][2]:,}")
    elif pilihan == "4" and flag:
        layer = 2
        return
    else:
        print("⚠️  Input tidak valid!")
        return printMenu(i_user)
    print()
    print("🛒 Apa yang ingin kamu lakukan selanjutnya?")
    print("1️⃣  Pesan")
    print("2️⃣  🔙 Kembali ke Menu")
    pilihan = input("📌 Pilihan: ")
    while pilihan not in ["1", "2"]:
        print("⚠️ Input salah!")
        pilihan = input("📌 Pilihan: ")

    if pilihan == "1":
        checkOut(i_user)
    else:
        printMenu(i_user)

# Kamus Data Lokal
# save_i : variabel parameter
# ask : variabel input pilihan fitur (str)
# redeem : variabel input nama menu yang akan ditukar dengan poin (str)
# found : variabel boolean
# i : variabel pengendali loop
# Fungsi ini berguna untuk user customer dalam menukar poin.
def redeemPoin(save_i):
    global layer
    print()
    print("🎁 PENUKARAN POIN")
    print("-"*100)
    print("1️⃣  Tukar Poin")
    print("2️⃣  🔙 Kembali ke menu utama")
    
    ask = input("📌 Pilih: ")
    while ask not in ["1", "2"]:
        print("⚠️ Input salah!")
        ask = input("📌 Pilih: ")

    if ask == "1":
        while True:
            redeem = input("📝 Nama menu yang ingin ditukar dengan poin: ")
            found = False
            for i in range(len(menu)):
                if redeem.lower() == menu[i][1].lower():
                    found = True
                    if poin[save_i][1] < (menu[i][2] * 0.05):
                        print("❌ Poin tidak mencukupi!")
                        return redeemPoin(save_i)
                    else:
                        poin[save_i][1] -= (menu[i][2] * 0.05)
                        print()
                        print(f"✅ Kamu berhasil menukar poin dengan {menu[i][1]}")
                        print(f"🧮 Sisa Poin: {poin[save_i][1]:.0f} pt")
                        return
            if not found:
                print("❌ Menu tidak tersedia!")
                print()
    else:
        layer = 2

# Kamus Data Lokal
# save_i : variabel parameter
# kategori : variabel kategori menu menu
# k : variabel pengendali loop
# i : variabel pengendali loop
# poin_diperlukan : variabel untuk menentukan suatu poin dari menu
# Fungsi ini berguna untuk user customer untuk menampilkan menu menu 
# dan harga poin dari suatu menu untuk ditukar serta total dari poin yang dimiliki.
def tukarPoin(save_i):
    print()
    print("🎁 DAFTAR MENU YANG DAPAT DITUKAR POIN")
    print("-"*100)

    kategori = {
        "noncoffee": "🥤 Non-Coffee",
        "coffee": "☕ Coffee",
        "makanan": "🍽️  Makanan",
        "dessert": "🍰 Dessert"
    }

    for k in kategori:
        print()
        print(f"{kategori[k]}")
        print("-"*100)
        for i in range(len(menu)):
            if menu[i][0] == k:
                poin_diperlukan = menu[i][2] * 0.05
                print(f" - {menu[i][1]:<40} {poin_diperlukan:.0f} Poin")
    print()
    print("-"*100)
    print(f"🪙  Poinmu saat ini: {poin[save_i][1]:.0f} pt")
    redeemPoin(save_i)

# Kamus Data Lokal
# save_i : variabel parameter
# i : variabel pengendali loop
# Fungsi ini berguna untuk user customer dalam menampilkan riwayat pembelian.
def history(save_i):
    print()
    print("📜 RIWAYAT PEMBELIAN")
    print("-"*100)

    if not allpay[save_i]:
        print("😌 Kamu belum pernah melakukan pembelian.")
    else:
        for i in range(len(riwayat[save_i])):
            print(f"{i+1}. {riwayat[save_i][i]:<30} Rp. {allpay[save_i][i]:,}")
        print("-"*100)
        print(f"💵 Total Harga       : Rp. {pendapatan[save_i][0]:,.0f}")
        print(f"🎁 Total Potongan    : Rp. {pendapatan[save_i][1]:,.0f}")
        print(f"🧾 Total yang Dibayar: Rp. {pendapatan[save_i][2]:,.0f}")

# Kamus Data Lokal
# admin, i_user : variabel parameter
# pilihan : variabel input pilihan fitur (str)
# Fungsi ini berguna untuk user admin dan customer untuk menampilkan
# fitur fitur yang akan digunakan oleh user masing-masing.
def home(admin, i_user):
    if admin:
        print()
        print("="*100)
        print("🏠 MENU UTAMA - ADMIN")
        print("="*100)
        print("1. 📊 Hitung Total Pendapatan")
        print("2. ➕ Tambah Menu")
        print("3. 📝 Ubah Harga Menu")
        print("4. 🎟️  Atur Kode Promo")
        print("5. 🚪 LogOut")
        print("-"*100)
        pilihan = str(input("👉 Pilihan Anda: "))
        if pilihan in ["1", "2", "3", "4","5"]:
            return int(pilihan)
        else:
            print("⚠️ Input tidak valid!")
            return 
    else:
        print()
        print("="*100)
        print("🏠 MENU UTAMA - PENGGUNA")
        print("="*100)
        print("1. 🍽️  Lihat Menu")
        print("2. 🎁 Tukar Poin")
        print("3. 📜 History Pembelian")
        print("4. 🚪 LogOut")
        print("-"*100)
        pilihan = str(input("👉 Pilihan Anda: "))
        if pilihan == "1":
            return int(pilihan)
        elif pilihan == "2":
            return int(pilihan)
        elif pilihan == "3":
            history(i_user)
        elif pilihan == "4":
            return int(pilihan)
        elif pilihan == "5":
            return int(pilihan)
        else:
            print("⚠️ Input tidak valid!")
            return 

# Kamus Data Lokal
# pilihan : variabel input pilihan fitur sign-up dan sign-in
# Fungsi ini berguna dalam memilih fitur untuk membuat akun atau masuk ke akun yang
# sudah pernah dibuat.
def awal():
    print()
    print("="*100)
    print("🛍️  SELAMAT DATANG DI LACCE COFFEE SHOP".center(100))
    print("="*100)
    print("1. ✍️  Sign Up")
    print("2. 🔐 Sign In")
    print("3. 🛑 Akhiri Program")
    print("-"*100)
    pilihan = str(input("👉 Pilihan Anda: "))
    while pilihan not in ["1", "2","3"]:
        print("⚠️  Input tidak valid!")
        pilihan = str(input("👉 Pilihan Anda: "))
    return int(pilihan)

# Kamus Data Lokal
# i_user : variabel parameter
# total_pay : variabel yang menyimpan total harga dari menu yang dipesan (int)
# kode : variabel input kode promo (str)
# diskon : variabel fungsi menghitung potongan pembelian
# Fungsi ini berguna untuk user customer dalam menampilkan total harga dari menu
# yang dipesan
def payment(i_user):
    global username
    print()
    print("-"*45)
    print("🧾 ORDERAN ANDA")
    print("-"*45)
    total_pay = 0
    for j in range(len(order[i_user])):
        print(f"{j+1}. {order[i_user][j]:<30} Rp. {pay[i_user][j]:,}")
        total_pay += pay[i_user][j]
    print("-"*45)
    print(f"💰 Total yang harus dibayar: Rp. {total_pay:,}")
    print("-"*45)

    kode = str(input("📦 Punya Kode Promo? [ya/tidak]: ")).lower()
    while kode not in ["ya", "tidak"]:
        print("⚠️ Input tidak valid!")
        kode = str(input("📦 Punya Kode Promo? [ya/tidak]: ")).lower()
    
    if kode == "ya":
        diskon = kodePromo()
        continuePay(diskon, total_pay, i_user)
    else:
        continuePay(0.0, total_pay, i_user)

# Kamus Data Lokal
# i_user : variabel parameter
# flag : variabel boolean
# check : variabel boolean
# pesan : variabel input nama menu yang akan dipesan (str)
# i : variabel pengendali loop
# ask : variabel input pesan lagi atau tidak (str)
# pilihan : variabel input pilihan fitur (str)
# Fungsi ini berguna untuk user customer dalam memesan suatu menu.
def checkOut(i_user):
    global order, username, pay
    flag = True
    while flag:
        check = False
        print()
        pesan = str(input("📝 Masukkan Pesanan: "))
        for i in range(len(menu)):
            if pesan in menu[i]:
                check = True
                print(f"✅ {menu[i][1]} berhasil ditambahkan ke pesanan kamu.")
                pay[i_user].append(menu[i][2])
                order[i_user].append(menu[i][1])
                flag = False
                break
        if not check:
            print("⚠️ Menu tidak tersedia!")

    ask = str(input("🔁 Pesan lagi? [ya] / [tidak]: ")).lower()
    while ask not in ["ya", "tidak"]:
        print("⚠️ Input salah!")
        ask = str(input("🔁 Pesan lagi? [ya] / [tidak]: ")).lower()

    if ask == "ya":
        checkOut(i_user)
    else:
        print()
        print("Apa yang ingin kamu lakukan selanjutnya?")
        print("1. 🔄 Pilih menu lain")
        print("2. 💳 Melakukan pembayaran")
        pilihan = input("👉 Pilihan Anda: ")
        while pilihan not in ["1", "2"]:
            print("⚠️ Input salah!")
            pilihan = input("👉 Pilihan Anda: ")
        if pilihan == "1":
            printMenu(i_user)
        elif pilihan == "2":
            payment(i_user)

# Kamus Data Lokal
# kode : variabel input kode promo (str)
# Fungsi ini berguna untuk user customer dalam menentukan kode promo yang 
# akan digunakan.
def kodePromo():
    global kupon

    kode = str(input("Masukkan Kode Promo: ")).upper()
    kategori = []
    for i in range(len(kupon)):
        if kupon[i][0] is not None :
            kategori.append(kupon[i][0])
    while kode not in kategori:
        print("❌ Kode Promo Salah! (atau ketik 'tidak jadi')")
        kode = str(input("Masukkan Kode Promo: ")).upper()
    for i in range (len(kupon)):
        if kupon[i][0] != None :
            if kode.upper() == kupon[i][0].upper():
                break
    diskon = kupon[i][1]
    return diskon
        

    

# Kamus Data Lokal
# potongan, total, save : variabel parameter
# harga_awal : variabel penyimpan nilai total (int)
# nilai_potongan : variabel total potongan pembelian yang didapatkan (int)
# harga_akhir : harga setelah total dikurangi potongan (int)
# bayar : variabel input nilai yang diberikan customer untuk membayar (int)
# kembalian : variabel untuk menyimpan nilai kembalian (int)
# Fungsi ini berguna untuk user customer dalam membayar total harga pesanan
# telah dipesan
def continuePay(potongan, total, save):
    harga_awal = total
    nilai_potongan = potongan * total
    harga_akhir = harga_awal - nilai_potongan
    print()
    print("🧾 RINCIAN PEMBAYARAN")
    print("-" * 100)
    if nilai_potongan == 0:
        print("❌ Tidak ada potongan")
    else:
        print(f"💸 Diskon         : Rp. {nilai_potongan:,.0f}")
        print(f"💰 Total Bayar    : Rp. {harga_akhir:,.0f}")
    print("-" * 100)

    bayar = int(input("💵 Masukkan nominal pembayaran: Rp. "))
    while bayar < harga_akhir:
        print(F"⚠️ Pembayaran kurang! Harus minimal Rp. {harga_akhir:,.0f}")
        bayar = int(input("💵 Masukkan ulang nominal pembayaran: Rp. "))

    if bayar > harga_akhir:
        kembalian = bayar - harga_akhir
        print(f"🎉 Pembayaran Berhasil! Kembalianmu: Rp. {kembalian:,.0f}")
    else:
        print("🎉 Pembayaran Berhasil!")

    pendapatan[save][0] += harga_awal
    pendapatan[save][1] += nilai_potongan
    pendapatan[save][2] += harga_akhir
    poin[save][1] += (harga_awal // 200)
    riwayat[save] += order[save]
    allpay[save] += pay[save]
    order[save] = []
    pay[save] = []

def main():
    global layer
    stop = False
    while stop != True :
        if layer == 1 :
            pilihan = awal()

            if (pilihan == 1):
                flag = signup()
                if (flag == True):
                    hasil = login()
                    admin = hasil[0]
            elif pilihan == 2 :
                hasil = login()
                admin = hasil[0]
            else :
                stop = True
        elif layer == 2 :
            pilihan = home(admin,hasil[1])
            if (pilihan == 1):
                if admin :
                    hitungTotal()
                else :
                    printMenu(hasil[1])
                    
            elif pilihan == 2 :
                if admin:
                    tambahMenu(admin,hasil[1])
                else:
                    tukarPoin(hasil[1])
            elif pilihan == 3 :
                if admin:
                    ubahHarga(admin,hasil[1])
                else:
                    history()
            elif pilihan == 4 :
                if admin == False:
                    layer = 1
                else :
                    aturKode()
            elif pilihan == 5 :
                if admin:
                    layer = 1
                
    return 0

if __name__ == '__main__': 
    # Kamus Data Global
    # layer : variabel penentu lapisan main
    # username : variabel array username (arr) {username[0] untuk admin}
    # password : variabel array password (arr) {password[0] untuk admin}
    # poin : variabel array poin yang dimiliki (arr) {poin[0] untuk admin}
    # menu : variabel array menu menu yang tersedia (arr)
    # order : variabel array menu yang dipesan perorderan oleh customer (arr)
    # riwayat : variabel array yang menyimpan semua menu yang pernah dipesan oleh setiap customer (arr)
    # allpay : variabel array yang menyimpan semua harga menu yang pernah dibayar oleh setiap customer (arr)
    # pay : variabel array menu yang dipesan perorderan oleh customer (arr)
    # pendapatan : variabel array yang menyimpan pendapatan (arr)
    #   {pendapatan[0] untuk pendapatan sebelum potongan}
    #   {pendapatan[1] untuk nilai potongan}
    #   {pendapatan[2] untuk pendapatan setelah diskon}
    # total : variabel array untuk menyimpan total pendapatan dari semua customer (arr)
    # subtotal : variabel array untuk menyimpan total belanja per customer (arr)
    layer = 1
    username = ["admin","noval"]
    password = ["admin123","noval123"]
    poin = [[None],["noval",100000]]
    menu = [
    ["coffee", "Espresso", 110000],
    ["coffee", "Cappuccino", 18000],
    ["coffee", "Cafe Latte", 18000],
    ["coffee", "Caramel Macchiato", 20000],
    ["coffee", "Iced Americano", 110000],

    ["noncoffee", "Matcha Latte", 18000],
    ["noncoffee", "Chocolate Milkshake", 20000],
    ["noncoffee", "Taro Latte", 18000],
    ["noncoffee", "Lemonade Sparkling", 110000],
    ["noncoffee", "Strawberry Smoothie", 18000],

    ["dessert", "Chocolate Lava Cake", 22000],
    ["dessert", "Strawberry Cheesecake", 22000],
    ["dessert", "Tiramisu Classic", 210000],
    ["dessert", "Banana Split", 18000],
    ["dessert", "Churros with Chocolate Dip", 110000],
    ["dessert", "Mango Sticky Rice", 20000],
    ["dessert", "Matcha Parfait", 20000],
    ["dessert", "Brownie Sundae", 20000],
    ["dessert", "Crepes Suzette", 23000],
    ["dessert", "Affogato", 110000],

    ["makanan", "Chicken Creamy Pasta", 30000],
    ["makanan", "Grilled Chicken Sandwich", 28000],
    ["makanan", "Beef Burger with Fries", 310000],
    ["makanan", "Nasi Goreng Cafe Style", 210000],
    ["makanan", "Caesar Salad with Grilled Chicken", 210000],
    ["makanan", "Fish & Chips", 32000],
    ["makanan", "Japanese Chicken Katsu Curry", 32000],
    ["makanan", "Creamy Mushroom Soup with Garlic Bread", 22000],
    ["makanan", "Baked Mac and Cheese", 210000],
    ["makanan", "Avocado Toast with Poached Egg", 23000]
    ]
    order = [[],[]]
    riwayat = [[],[]]    
    allpay = [[],[]]
    pay = [[],[]]
    pendapatan = [[],[0,0,0]]
    total = 0
    subtotal = [0,0]
    kupon = [["MURMERLACCE10",0.1],["MURMERLACCE20",0.2],["MURMERLACCE30",0.3],["TIDAK JADI",0.0]]
    main()   