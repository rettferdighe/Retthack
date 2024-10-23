import os
import time
from colorama import init, Fore
import webbrowser



init(autoreset=True)


while True:
    os.system("clear || cls")
    print(Fore.RED + "   ___     ___    _____   _____   _  _     ___     ___    _  __ ")
    print(Fore.RED + "  | _ \   | __|  |_   _| |_   _| | || |   /   \   / __|  | |/ / ")
    print(Fore.RED + "  |   /   | _|     | |     | |   | __ |   | - |  | (__   | ' <")
    print(Fore.RED + "  |_|_\   |___|   _|_|_   _|_|_  |_||_|   |_|_|   \___|  |_|\_\ \n\n")
    print(Fore.YELLOW + "Instagram: rettvirtuall\t\t\t\t Youtube: retthack\n\n")
    secim = input(Fore.BLUE+
        "1-) Tren geçişi (Termux | Linux)"
        "2-) Şömine (Termux | Linux)\n"
        "3-) ASCII nickname (Termux | Linux)\n"
        "4-) Matrix ekranı (Termux | Linux)\n"
        "5-) Sistem bilgilerini gösterir (Termux | Linux)\n"
        "6-) Metni sese çevirme (Termux)\n"
        "7-) Speedtest (Termux | Linux)\n"
        "8-) Araba oyunu (Termux | Linux)\n"
        "9-) Çeviri (Termux)\n"
        "10-) Nyancat (Termux | Linux)\n"
        "11-) Filmlerdeki hack sahnesi arayüzü (Termux | Linux)\n"
        "12-) Instagram\n"
        "Bir numara seçiniz: "
    )

    if secim == "1":
        os.system("pkg install sl -y||apt-get install sl -y"),
        os.system("sl")

    elif secim == "2":
        os.system("pkg install libcaca -y||apt-get install cacafire -y")
        os.system("cacafire")

    elif secim == "3":
        annen = input("Nickname giriniz: ")
        os.system("pkg install figlet -y||apt-get install figlet -y")
        os.system(f"figlet {annen}")
        input("devam etmek icin 'Enter' tuşuna basınız")
    elif secim == "4":
        os.system("pkg install cmatrix -y||apt-get install cmatrix -y")
        os.system("cmatrix")

    elif secim == "5":
        os.system("pkg install neofetch -y||apt-get install netofetch -y")
        os.system("neofetch")
        input("devam etmek icin 'Enter' tusuna basiniz")
    elif secim == "6":
        baban = input("Sese çevrilecek metni giriniz: ")
        os.system("pkg install espeak -y")
        os.system(f'espeak "{baban}"')

    elif secim == "7":
        os.system("pkg install speedtest-go -y||apt-get install sppedtest-cli -y")
        os.system("speedtest-go")

    elif secim == "8":
        os.system("pkg install moon-buggy -y||apt-get install moon-buggy -y")
        os.system("moon-buggy")

    elif secim == "9":
        trans = input("çevirilecek cümleyi giriniz: ")
        os.system("pkg install translate-shell -y ")
        os.system(f'trans -b :tr "{trans}"')
        input("devam etmek icin 'Enter' tusuna basiniz")

    elif secim == "10":
        os.system("pkg install nyancat||apt-get install nyancat -y")
        os.system("nyancat")

    elif secim == "11":
        os.system("pkg install hollywood -y||apt-get install hollywood -y")
        os.system("hollywood")

    elif secim == "12":
        webbrowser.open("https://instagram.com/rettvirtuall")

    else:
        print("geçersiz bir numara girdiniz. Lütfen tekrar deneyin.")
        time.sleep(2)
