ad = input("Adinizi giriniz:")
soyad = input("Soyisminizi giriniz:")
numara = input("Ogrenci numaranizi giriniz:")
print('Adiniz:{}, Soyadiniz:{}, Ogrenci Numaraniz:{}'.format(ad,soyad,numara)) #Tek bir print komutu ile ilk basta istenen 3 bilgiyi yazdirmak icin bu metodu kullandim.
dersler= ["Fizik", "Kimya", "Matematik", "Muzik"]
for i in dersler:
    print(i)
    vize= int(input("Vize notunuzu giriniz:"))
    final= int(input("Final notunuzu giriniz:"))

print("\nDerslerin ortalamasi:")
for ortalama in dersler:
    ortalama = vize * 0.4 + final * 0.6
    print(ortalama)
    if ortalama >= 50:
        print("Tebrikler Gectiniz.")
    else:
        print("Kaldiniz.")



