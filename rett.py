import os
import time
import pytube


while True:
    os.system("clear")
    print("   ___     ___    _____   _____   _  _     ___     ___    _  __ ")
    print("  | _ \   | __|  |_   _| |_   _| | || |   /   \   / __|  | |/ / ")
    print("  |   /   | _|     | |     | |   | __ |   | - |  | (__   | ' <")
    print("  |_|_\   |___|   _|_|_   _|_|_  |_||_|   |_|_|   \___|  |_|\_\ ")
    secim = input(
        "1-) Tren geçişi\n"
        "2-) Şömine\n"
        "3-) ASCII nickname\n"
        "4-) Matrix ekranı\n"
        "5-) Sistem bilgilerini gösterir\n"
        "6-) Metni sese çevirme\n"
        "7-) Speedtest\n"
        "8-) Araba oyunu\n"
        "9-) Çeviri\n"
        "Bir numara seçiniz: "
    )

    if secim == "1":
        os.system("pkg install sl -y")
        os.system("sl")
        break
    elif secim == "2":
        os.system("pkg install libcaca -y")
        os.system("cacafire")
        break
    elif secim == "3":
        annen = input("Nickname giriniz: ")
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
        baban = input("Sese çevrilecek metni giriniz: ")
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
    elif secim == "9":
        trans = input("çevirilecek cümleyi giriniz: ")
        os.system("pkg install translate-shell -y ")
        os.system(f'trans -b :tr "{trans}"')
        break
    else:
        print("geçersiz bir numara girdiniz. Lütfen tekrar deneyin.")
        time.sleep(2)
