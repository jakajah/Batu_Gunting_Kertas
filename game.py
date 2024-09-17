import random

# Input
print(3 * "#" + " Batu Gunting Kertas " + 3 * "#")
username = input("Silakan Masukan Username: ")
koin = int(input("Silakan Masukan Koin Anda: "))

# Pilihan komputer
pilihan_komputer = ["1", "2", "3"]

# Looping permainan sampai koin habis
while koin >= 20:
    print(f"\nKoin kamu: {koin} koin")
    print(3 * "#" + " Permainan Dimulai " + 3 * "#")
    print("""Silakan Pilih salah satu !!!
      >1. Kertas
      >2. Gunting
      >3. Batu""")
    
    # Input dari pengguna
    inputuser = input("Silakan Pilih : ").capitalize()

    # Pilihan komputer secara acak
    komputer = random.choice(pilihan_komputer)
    # Menampilkan pilihan permainan
    # pilihan user 
    if inputuser in "1" :
        print(f"{username} memilih : Kertas")
    if inputuser in "2" :
        print(f"{username} memilih : Gunting")
    if inputuser in "3" :
        print(f"{username} memilih : Batu")
    # pilihan komputer
    if komputer in "1" :
        print(f"Komputer memilih : Kertas")
    if komputer in "2" :
        print(f"Komputer memilih : Gunting")
    if komputer in "3" :
        print(f"Komputer memilih : Batu")

    # Inti permainan (penentuan pemenang)
    if inputuser == komputer:
        print("Hasil: Seri!")
    elif (inputuser == "3" and komputer == "2") or \
         (inputuser == "2" and komputer == "1") or \
         (inputuser == "1" and komputer == "3"):
        print(f"{username} menang!")
        koin += 10  # Menambahkan 10 koin jika menang
    elif (inputuser == "3" and komputer == "1") or \
         (inputuser == "2" and komputer == "3") or \
         (inputuser == "1" and komputer == "2"):
        print("Komputer menang, kamu kalah!")
        koin -= 20 # Mengurangi 20 koin jika menang 

    else:
        print("Pilihan tidak valid, coba lagi.")
        continue  # Jika pilihan tidak valid, ulangi tanpa mengurangi koin


    # Cek apakah koin masih mencukupi untuk bermain lagi
    if koin < 20:
        print(f"Koinmu sekarang {koin}, kamu tidak cukup koin untuk bermain lagi.")
        break  # Keluar dari loop jika koin habis
    else:
        print(f"Koin tersisa: {koin}, ayo main lagi!")

print(f"Permainan selesai. Terima kasih sudah bermain, {username}!")
