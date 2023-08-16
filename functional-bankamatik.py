# Hesap Bilgileri

pin = "1234"
bakiye = 2000


# Bakiye Sorgula

def bakiye_sorgula():
    print("Mevcut Bakiye: ", bakiye)

# Para Çek

def para_cek():
    miktar = float(input("Çekmek istediğiniz miktarı giriniz: "))
    if (miktar <= bakiye):
        bakiye -= miktar
        print("Çekilen miktar: ", miktar)
        print("Kalan Bakiyeniz: ", bakiye)
    else:
        print("Geçersiz Bakiye...")

# Para Yatır

def para_yatir():
    miktar = float(input("Yatıracağınız miktarı giriniz: "))
    bakiye += miktar
    print("Güncel Bakiyeniz: ", bakiye)

# Hesap Bilgilerini Güncelleme

def hesap_guncelleme():
    name = input("Yeni Ad: ")
    surname = input("Yeni Soyad: ")
    print(f"Yeni isim: {name}, Yeni Soyad: {surname}")


# Atm Çıkış

def atm_cikis():
    print("ATM'den çıkış yapılıyor......")
    exit()



while True:
    giris = input("PIN Giriniz: ")
    if (giris == pin):
        print("Hesabınıza başarıyla giriş yaptınız...")
        break
    else:
        print("Geçersiz PIN.Tekrar deneyiniz...")

while True:
    print("---------- ATM Menüsü ----------")
    print("1. Bakiye Sorgula")
    print("2. Para Çek")
    print("3. Para Yatır")
    print("4. Hesap Bilgilerini Güncelle")
    print("5. ATM'den Çıkış Yap.")
    secim = int(input("Seçiminizi Yapınız: "))

    if (secim == 1):
        bakiye_sorgula()

    elif (secim == 2):
        para_cek()

    elif (secim == 3):
        para_yatir()

    elif (secim == 4):
        hesap_guncelleme()

    elif (secim == 5):
        atm_cikis()

    else:
        print("Geçersiz Seçim....")