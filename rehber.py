import sqlite3

baglanti = sqlite3.connect("telrehber.db")
islem = baglanti.cursor()
tablo= "CREATE TABLE IF NOT EXISTS kisiler(AD TEXT,SOYAD TEXT,NUMARA INT)"
islem.execute(tablo)
baglanti.commit()

def baglanti_kes():
    baglanti.close()

def kisileri_listele():
  goster ="SELECT *FROM kisiler"
  islem.execute(goster)
  kisiler =islem.fetchall()
  if len(kisiler)==0:
        print("Sistemde kayıtlı kimse yok")
  else:
    for i in kisiler:
        print(i)

def kisi_ekle(AD,SOYAD,NUMARA):
    ekle= "INSERT INTO kisiler (AD,SOYAD,NUMARA) VALUES(?,?,?)"
    islem.execute(ekle(AD,SOYAD,NUMARA))
    baglanti.commit()

def kisi_sil(NUMARA):
 sorgu="DELETE FROM kisiler WHERE NUMARA = ?"
 islem.execute(sorgu,(NUMARA,))
 baglanti.commit()

def kisi_bul(NUMARA):
  sorgu="SELECT * FROM kisiler WHERE NUMARA =?"
  islem.execute(sorgu,(NUMARA,))
  kisiler =islem.fetchall()
  if len(kisiler)==0:
    print("Aranılan Kişi Sistemde Bulunmamaktadır..")
  else:
    print(kisiler)

print("""
**************************************
1. Ekleme
2. Arama
3. Listeleme
4. Silme
q. Çıkış
**************************************
""")

while True:
 secim= input("Bir işlem seçin :")
 if secim=="q":
    print("Çıkış Yapıldı")
    baglanti_kes()
    break
 elif secim=="1":
    AD = input("İsim :")
    SOYAD = input("Soyisim :")
    NUMARA = int(input("Numara :"))
    kisi_ekle(AD,SOYAD,NUMARA)
    print("Kişi Eklendi")

 elif secim=="2":
     no =input("Aranacak kişinin kayıt no: ")
     print("Kişi sorgulanıyor ...")
     kisi_bul(NUMARA)

 elif secim=="3":
     kisileri_listele()

 elif secim=="4":
      NUMARA =int(input("Silinecek kişinin kayıt no: "))
      tekrar =input("Kaydı silmek istediğinizden emin misiniz(E/H):")
      if tekrar=="E":
         print("Kayıt Silindi")
      kisi_sil(NUMARA)
 else:
     print("Geçersiz işlem")