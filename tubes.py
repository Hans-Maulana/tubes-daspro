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
    return True


def login():
    global username, password
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
            login()
        else :
            print("Login Berhasil!")
    arr = [flag,user]
    return arr

def tambahMenu():
    ew= 0   

def hitungTotal():
    ew= 0   

def ubahHarga():
    ew= 0   
    
def printMenu():
    global menu
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
    else :
        check = False
        print("Input Salah!")
        printMenu()
    
    if check :
        print()
        print("1. Pesan")
        print("2. Ke halaman Menu")
        pilihan = str(input("Pilihan : "))
        while pilihan != "1" and pilihan != "2":
            print("input salah!")
            pilihan = str(input("Pilihan : "))
        
        if pilihan == "1" :
            return True
        else :
            printMenu()
       



def tukarPoin():
    ew = 0

def history():
    ew = 0

def home(admin):
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
            home()
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
            return int(pilihan)
        elif pilihan == "4":
            awal()
        else :
            print("Input Salah!")
            home()

def awal():
    print("==================================")
    print("1. Sign Up")
    print("2. Sign In")
    print("==================================")
    pilihan = str(input("Pilihan : "))
    while(pilihan != "1" and pilihan != "2"):
        print("Input salah!")
        pilihan = str(input("Pilihan : "))
    return pilihan

def checkOut(nama):
    global order,username,pay
    flag = True
    while(flag):
        pesan = str(input('Masukkan Pesanan:'))
        for i in range(len(menu)):
            if pesan in menu[i]:
                check = True
                print(f"{menu[i][1]} ditambahkan Ke pesanan Kamu")
                for j in range (len(username)):
                    if nama == username[j]:
                        pay[j].append(menu[i][2])
                        order[j].append(menu[i][1])
                        break 
                flag = False
                break
        if check == False :
            print("Menu tidak tersedia!")


    ask = str (input('Pesan lagi? [ya] | [tidak] : '))
    if (ask == "ya"):
        checkOut(nama)
    else :
        print()
        print('1. Pilih menu lain')
        print('2. Melakukan pembayaran')
        pilihan = str(input('Pilihan : '))
        while pilihan != '1' and pilihan != '2':
            print("input salah!")
            pilihan = str(input('Pilihan : '))
        if pilihan == '1':
            return int(pilihan)  
        else:
            return int(pilihan)                

def payment(nama):
    global username
    print()
    print("Orderan")
    print("------------------------------------------")
    for i in range (len(username)):
        if nama == username[i]:
            for j in range(len(order[i])):
                print(f"{j+1}. {order[i][j]} - Rp.{pay[i][j]}")
            break
        



    
def main():
    pilihan = awal()

    if (pilihan == "1"):
        flag = signup()
        if (flag == True):
            hasil = login()
            admin = hasil[0]
    else :
        hasil = login()
        admin = hasil[0]

    pilihan = home(admin)
    if (pilihan == 1):
        if admin :
            hitungTotal()
        else :
            flag = printMenu()
            if flag :
                pilih = checkOut(hasil[1])
                if pilih == 1 :
                    printMenu()
                else :
                    payment(hasil[1])

    elif pilihan == 2 :
        if admin:
            tambahMenu()
        else:
            tukarPoin()
    elif pilihan == 3 :
        if admin:
            ubahHarga()
        else:
            history()
            

# Perintah Input    
# Perintah Proses
    
# Perintah Output
    return 0

if __name__ == '__main__':   
    username = ["admin","noval"]
    password = ["admin123","noval123"]
    poin = [[None],["noval",100]]
    menu = [
    ["coffee", "Espresso", 15000],
    ["coffee", "Cappuccino", 18000],
    ["coffee", "Café Latte", 18000],
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
    pay = [[],[]]
    main()   