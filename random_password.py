import random
import string

def rastgele_sifre_olustur(uzunluk):
    karakterler = string.ascii_letters + string.digits + string.punctuation
    rastgele_sifre = ''.join(random.choice(karakterler) for i in range(uzunluk))
    return rastgele_sifre

if __name__ == "__main__":
    try:
        uzunluk = int(input("Şifre uzunluğunu girin: "))
        if uzunluk <= 0:
            print("Geçersiz uzunluk. Pozitif bir tamsayı girin.")
        else:
            sifre = rastgele_sifre_olustur(uzunluk)
            print("Oluşturulan rastgele şifre:", sifre)
    except ValueError:
        print("Hatalı giriş. Pozitif bir tamsayı girin.")
