import os
import time

while True:
    os.system("clear")
    secim = input("1-) Tren gecişi\n2-) Şömine\n3-) ASCII nickname\n4-) Matrix ekranı\n5-) Sistem bilgilerini gösterir\n6-) Metni sese çevirme\n7-) Speedtest\n8-) Araba oyunu\nbir numara seçiniz: ")

    if secim == "1":
        os.system("pkg install sl -y")
        os.system("sl")
        break
    elif secim == "2":
        os.system("pkg install libcaca -y")
        os.system("cacafire")
        break
    elif secim == "3":
	annen = input("nickname giriniz: ")
        os.system("pkg install figlet -y")
        os.system(f"figlet {annen}")
        break
    elif secim == "4":
        os.system("pkg install cmatrix -y")
        os.system("cmatrix")
        break
    elif secim == "5":
        os.system("pkg install neofetch -y")
        os.system("neofetch")
        break
    elif secim == "6":
        baban = input("sese çevirilecek metni giriniz: ")
        os.system("pkg install espeak -y")
        os.system(f'espeak "{baban}"')
        break
    elif secim == "7":
        os.system("pkg install speedtest-go -y")
        os.system("speedtest-go")
        break
    elif secim == "8":
        os.system("pkg install moon-buggy -y")
        os.system("moon-buggy")
        break
    else:
        print("Geçersiz bir numara girdiniz. Lütfen tekrar deneyin.")
        time.sleep(2)