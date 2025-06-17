# File : <namafile..py 
# Penulis : <nama>
# Tujuan Program
# Kamus Data
def signup():
    global username, password
    print()
    print("Sign Up")
    user = str(input("Buat Username : "))
    pw = str(input("Buat Password : "))
    if user in username :
        print("Username tidak tersedia")
        signup()
    else :
        username.append(user)
        password.append(pw)
        order.append([])
        riwayat.append([])   
        pay.append([])
        allpay.append([])
        subtotal.append(0)
        pendapatan.append([0,0,0])
        poin.append([user,0])
    return True

def login():
    global username, password,layer
    i = 0
    print()
    print("Sign In")
    user = str(input("Username : "))
    pw = str(input("Password : "))
    if(user == username[0] and pw == password[0]):
        flag = True
        print("Login Sebagai Admin")
    else:
        for i in range (len(username)):
            if (user == username[i] and pw == password[i]):
                flag = False
                mark = True
                break
            else :
                mark = False
        if (mark == False):
            print("Username atau Password Salah!")
            flag = False
            login()
        else :
            print("Login Berhasil!")
    arr = [flag,i]
    layer = 2
    return arr

def tambahMenu(admin,i_user):
    global menu,layer
    while True:
        print()
        print("=== Tambah Menu Baru ===")
        print("1. Makanan")
        print("2. Minuman")
        print("3. Dessert")
        print("4. Kembali ke Home")
        print()
        pilihan = input("Pilih kategori menu : ")

        if pilihan == "1":
            kategori = "makanan"
        elif pilihan == "2":
            print("1. Coffee")
            print("2. Non-Coffee")
            minuman = input("Jenis Minuman : ")
            while minuman not in ["1","2"]:
                print("input tidak valid")
                minuman = input("Jenis Minuman:")
            if (minuman == "1"):
                kategori = "coffee"
            elif (minuman  == "2") :
                kategori = "noncoffee"
        elif pilihan == "3":
            kategori = "dessert"
        elif pilihan == "4":
            layer = 2 
        else:
            print("Pilihan tidak valid. Coba lagi.")

        nama = input("Nama Menu : ")
        harga = input("Harga (Rp): ")
        while not harga.isdigit():
            print("Harga harus berupa angka.")
            harga = input("Harga (Rp): ")
        harga = int(harga)
        
        menu.append([kategori, nama, harga])
        print(f"Menu {nama} berhasil ditambahkan ke kategori {kategori}")

        ulang = input("Tambah menu lagi? [ya] | [tidak] : ").lower()
        if ulang != 'ya':
            layer = 2
    
def hitungTotal():
    global riwayat,allpay,total,subtotal,layer,pendapatan
    print()
    print("Hasil Pendapatan :")   
    print("===========================================")
    total = 0
    diskon = 0
    for i in range (len(riwayat)-1):
        i += 1
        print()
        print("Username :",username[i])
        print("------------------------------")
        print(f"{'Nama Barang' :<20} Harga")
        for j in range(len(riwayat[i])):
            print(f"{riwayat[i][j]:<20} {allpay[i][j]}")
            total += allpay[i][j]
        
        print(f"Total diskon : Rp. {pendapatan[i][1]}")
        print(f"Total Pembayaran : Rp. {pendapatan[i][2]} ")
        print("------------------------------")
        diskon += pendapatan[i][1]
    print(f"Total pendapatan : Rp. {total-diskon}")
    layer = 2
    return
    



def ubahHarga(admin,i_user):
    global menu,layer

    while True:
        print()
        print("=== Ubah Harga Menu ===")
        print("1. Minuman")
        print("2. Makanan")
        print("3. Dessert")
        print("4. Kembali ke Home")
        print()
        
        pilihan = str(input("Pilihan : "))
        check = True
        if pilihan == "1":
            print()
            print("Menu Non Coffee")
            for i in range(len(menu)):
                if "noncoffee" in menu[i]:
                    print(f"{menu[i][1]:<20} Rp.{menu[i][2]}")
            print()
            print("Menu Coffee")
            for i in range(len(menu)):
                if "coffee" in menu[i]:
                    print(f"{menu[i][1]:<20} Rp.{menu[i][2]}")
        elif pilihan == "2":
            print()
            print("Menu Makanan")
            for i in range(len(menu)):
                if "makanan" in menu[i]:
                    print(f"{menu[i][1]:<40} Rp.{menu[i][2]}")
        elif pilihan == "3":
            print()
            print("Menu Dessert")
            for i in range(len(menu)):
                if "dessert" in menu[i]:
                    print(f"{menu[i][1]:<30} Rp.{menu[i][2]}")
        elif pilihan == "4":
            layer = 2
        else :
            check = False
            print("Input Salah!")
            printMenu(i_user)

        flag = True
        while(flag):
            check = False
            ganti = str(input('Masukkan Nama Menu:'))
            for i in range(len(menu)):
                if ganti in menu[i]:
                    check = True
                    print(f"Menu yang dipilih: {menu[i][1]} (Harga saat ini: Rp. {menu[i][2]})")
                    flag = False
                    break
            if check == False :
                print("Menu tidak tersedia!")
        
        harga_input = input("Masukkan harga baru: ")
        while not harga_input.isdigit():
            print("Harga harus berupa angka.")
            harga_input = input("Masukkan harga baru: ")
        harga_baru = int(harga_input)

        menu[i][2] = harga_baru
        print(f"Harga menu '{menu[i][1]}' berhasil diubah menjadi Rp{harga_baru}")

        ulang = input("Tambah menu lagi? [ya] | [tidak] : ").lower()
        if ulang != 'ya':
            home(admin,i_user)


def printMenu(i_user):
    global menu
    if not order[i_user]:
        flag = True
    else :
        flag = False
    if flag :
        print()
        print("1. Minuman")
        print("2. Makanan")
        print("3. Dessert")
        print("4. Kembali Ke halaman utama")
    else :
        print()
        print("1. Minuman")
        print("2. Makanan")
        print("3. Dessert")
    pilihan = str(input("Pilihan : "))
    check = True
    
    if pilihan == "1":
        print()
        print("Menu Non Coffee")
        for i in range(len(menu)):
            if "noncoffee" in menu[i]:
                print(f"{menu[i][1]:<20} Rp.{menu[i][2]}")
        print()
        print("Menu Coffee")
        for i in range(len(menu)):
            if "coffee" in menu[i]:
                print(f"{menu[i][1]:<20} Rp.{menu[i][2]}")
    elif pilihan == "2":
        print()
        print("Menu Makanan")
        for i in range(len(menu)):
            if "makanan" in menu[i]:
                print(f"{menu[i][1]:<40} Rp.{menu[i][2]}")
    elif pilihan == "3":
        print()
        print("Menu Dessert")
        for i in range(len(menu)):
            if "dessert" in menu[i]:
                print(f"{menu[i][1]:<30} Rp.{menu[i][2]}")
    elif pilihan == "4" and flag == True:
        layer = 2
        return
    else :
        check = False
        print("Input Salah!")
        printMenu(i_user)
    
    print()
    print("1. Pesan")
    print("2. Ke halaman Menu")
    pilihan = str(input("Pilihan : "))
    while pilihan != "1" and pilihan != "2":
        print("input salah!")
        pilihan = str(input("Pilihan : "))
    
    if pilihan == "1" :
        checkOut(i_user)
    else :
        printMenu(i_user)

def redeemPoin(save_i):
    global layer
    print()
    print("1. Tukar Poin")
    print("2. Kembali ke menu utama")
    ask = str(input("Pilih : "))
    while ask not in ["1","2"]:
        print ("Input salah!")
        ask = str(input("Pilih : "))
    if ask == "1":
        ada = False
        while ada == False :
            redeem = str(input("Tukar Poin : "))
            for i in range(len(menu)):
                if redeem in menu[i]:
                    ada = True
                    break
            if ada :
                if ((menu[i][2]*0.05) > poin[save_i][1]):
                    print("Poin tidak mencukupi!")
                    redeemPoin(save_i)
                else:
                    print()
                    poin[save_i][1] -= (menu[i][2]*0.05)
                    print (f"Kamu Berhasil Menukar Poin dengan {menu[i][1]}")
                    print (f"Sisa poinmu : {poin[save_i][1]:.0f}pt")
                    
            else :
                print("Menu Tidak Tersedia!")
                print()
    else:
        layer = 2

def tukarPoin(save_i):
    print("Penukaran Poin")
    print("==================================================")
    print()
    print("Menu Non Coffee")
    print("--------------------------------------------------")
    for i in range(len(menu)):
            if "noncoffee" in menu[i]:
                print(f"{menu[i][1]:<40} {menu[i][2]*0.05:.0F} Poin")
    print()
    print("Menu Coffee")
    print("--------------------------------------------------")
    for i in range(len(menu)):
            if "coffee" in menu[i]:
                print(f"{menu[i][1]:<40} {menu[i][2]*0.05:.0F} Poin")
    print()
    print("Menu Makanan")
    print("-------------------------------------------------")
    for i in range(len(menu)):
            if "makanan" in menu[i]:
                print(f"{menu[i][1]:<40} {menu[i][2]*0.05:.0F} Poin")
    print()
    print("Menu Dessert")
    print("-------------------------------------------------")
    for i in range(len(menu)):
        if "dessert" in menu[i]:
            print(f"{menu[i][1]:<40} {menu[i][2]*0.05:.0F} Poin")
    print("=================================================")
    print(f"Poin Mu : {poin[save_i][1]}pt")
    redeemPoin(save_i)
    
def history(save_i):
    print()
    if not allpay[save_i] :
        print("Kamu belum pernah melakukan pembelian nih🤗")
    else:
        for i in range (len(riwayat[save_i])):
            print(f"{i+1}. {riwayat[save_i][i]} ----------- Rp.{allpay[save_i][i]}") 
        print("---------------------------------------------------------------------")
        print(f"Total Harga :",pendapatan[save_i][0])
        print(f"Total Potongan :",pendapatan[save_i][1])
        print(f"Total Yang Dibayar :",pendapatan[save_i][2])
    return


def home(admin,i_user):
    if admin :
        print()
        print("Pilihan Menu")
        print("1. Hitung Total Pendapatan")
        print("2. Tambah Menu")
        print("3. Ubah Harga Menu")
        print("4. LogOut")
        pilihan = str(input("Pilihan : "))
        if pilihan == "1":
            return int(pilihan)
        elif pilihan == "2":
            return int(pilihan)
        elif pilihan == "3":
            return int(pilihan)
        elif pilihan == "4":
            return int(pilihan)
        else :
            print("Input Salah!")
            home(admin,i_user)
    else :
        print()
        print("Pilihan Menu")
        print("1. Menu")
        print("2. Tukar Poin")
        print("3. History Pembelian")
        print("4. LogOut")
        pilihan = str(input("Pilihan : "))
        if pilihan == "1":
            return int(pilihan)
        elif pilihan == "2":
            return int(pilihan)
        elif pilihan == "3":
            history(i_user)
        elif pilihan == "4":
            return int(pilihan)
        else :
            print("Input Salah!")
            home(admin,i_user)

def awal():
    print("==================================")
    print("1. Sign Up")
    print("2. Sign In")
    print("==================================")
    pilihan = str(input("Pilihan : "))
    while(pilihan != "1" and pilihan != "2"):
        print("Input salah!")
        pilihan = str(input("Pilihan : "))
    return int(pilihan)

def payment(i_user):
    global username
    print()
    print("Orderan")
    print("------------------------------------------")
    total = 0
    for j in range(len(order[i_user])):
        print(f"{j+1}. {order[i_user][j]} - Rp.{pay[i_user][j]}")
        total +=pay[i_user][j]
    print(f"Total Yang Harus Dibayar : {total}")
    print()
    kode = str(input("Punya Kode Promo? [ya] [tidak] :"))
    while kode not in ["ya","tidak"]:
        print("input salah!")
        kode = str(input("Punya Kode Promo? [ya] [tidak] :"))
    if kode == "ya":
        diskon = kodePromo()
        continuePay(diskon,total,i_user)
    else:
        continuePay(0.0,total,i_user)
        
def checkOut(i_user):
    global order,username,pay
    flag = True
    while(flag):
        check = False
        pesan = str(input('Masukkan Pesanan:'))
        for i in range(len(menu)):
            if pesan in menu[i]:
                check = True
                print(f"{menu[i][1]} ditambahkan ke pesanan Kamu")
                pay[i_user].append(menu[i][2])
                order[i_user].append(menu[i][1])
                
                flag = False
                break
        if check == False :
            print("Menu tidak tersedia!")

    ask = str (input('Pesan lagi? [ya] | [tidak] : '))
    while ask not in ["ya","tidak"]:
        print("input salah!")
        ask = str (input('Pesan lagi? [ya] | [tidak] : '))

    if (ask == "ya"):
        checkOut(i_user)
    else :
        print()
        print('1. Pilih menu lain')
        print('2. Melakukan pembayaran')
        pilihan = input('Pilihan : ')
        while pilihan not in ["1","2"]:
            print("input salah!")
            pilihan = input('Pilihan : ')
        print(pilihan)
        if pilihan == '1':
            printMenu(i_user)
        elif pilihan == '2':
            payment(i_user)
              
def kodePromo():
    kode = str(input("Input kode promo : "))
    while kode not in ["MURMERLACCE10","MURMERLACCE20","MURMERLACCE30","tidak jadi"]:
        print("Kode Promo Salah! isi [tidak jadi] :")
        kode = str(input("Input kode promo : "))
    if kode == "MURMERLACCE10":
        diskon = 0.1
    elif kode == "MURMERLACCE20":
        diskon = 0.2
    elif kode == "MURMERLACCE30":
        diskon = 0.3
    elif kode == "tidak jadi":
        diskon = 0.0
        
    return diskon

def continuePay(potongan,total,save):
    harga = total
    potongan *= total
    harga -= potongan
    if harga == total:
        print("tidak ada potongan")
        print(f"harga yang harus dibayar : {harga} ")
    else :
        print(f"Diskon : Rp.{potongan}")
        print(f"Harga setelah Diskon : Rp.{harga}")
    bayar = int(input("Masukkan nominal pembayaran : Rp."))
    while (bayar < harga):
        print("Pembayaran Kurang, masukkan nominal >= harga yang harus bayar")
        bayar = int(input("Masukkan nominal pembayaran : Rp."))
    if bayar > harga:
        kembalian =  bayar - harga
        print(f"Kembalian : Rp.{kembalian}")
        print("Pembayaran Berhasil!")
    else :
        print("Pembayaran Berhasil!")
    pendapatan[save][2] += harga
    pendapatan[save][1] += potongan
    pendapatan[save][0] += total
    poin[save][1] += (total//200)
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
            else :
                hasil = login()
                admin = hasil[0]
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
                layer = 1
    return 0

if __name__ == '__main__': 
    layer = 1
    username = ["admin","noval"]
    password = ["admin123","noval123"]
    poin = [[None],["noval",100000]]
    menu = [
    ["coffee", "Espresso", 15000],
    ["coffee", "Cappuccino", 18000],
    ["coffee", "Cafe Latte", 18000],
    ["coffee", "Caramel Macchiato", 20000],
    ["coffee", "Iced Americano", 15000],

    ["noncoffee", "Matcha Latte", 18000],
    ["noncoffee", "Chocolate Milkshake", 20000],
    ["noncoffee", "Taro Latte", 18000],
    ["noncoffee", "Lemonade Sparkling", 15000],
    ["noncoffee", "Strawberry Smoothie", 18000],

    ["dessert", "Chocolate Lava Cake", 22000],
    ["dessert", "Strawberry Cheesecake", 22000],
    ["dessert", "Tiramisu Classic", 25000],
    ["dessert", "Banana Split", 18000],
    ["dessert", "Churros with Chocolate Dip", 17000],
    ["dessert", "Mango Sticky Rice", 20000],
    ["dessert", "Matcha Parfait", 20000],
    ["dessert", "Brownie Sundae", 20000],
    ["dessert", "Crepes Suzette", 23000],
    ["dessert", "Affogato", 15000],

    ["makanan", "Chicken Creamy Pasta", 30000],
    ["makanan", "Grilled Chicken Sandwich", 28000],
    ["makanan", "Beef Burger with Fries", 35000],
    ["makanan", "Nasi Goreng Cafe Style", 27000],
    ["makanan", "Caesar Salad with Grilled Chicken", 27000],
    ["makanan", "Fish & Chips", 32000],
    ["makanan", "Japanese Chicken Katsu Curry", 32000],
    ["makanan", "Creamy Mushroom Soup with Garlic Bread", 22000],
    ["makanan", "Baked Mac and Cheese", 27000],
    ["makanan", "Avocado Toast with Poached Egg", 23000]
    ]
    order = [[],[]]
    riwayat = [[],[]]    
    allpay = [[],[]]
    pay = [[],[]]
    pendapatan = [[],[0,0,0]]
    total = 0
    subtotal = [0,0]
    main()   