import random
def tebak_angka():
    print("game angka")

    mode = input("Pilih mode kesulitan (mudah, sedang, sulit): ")
    if mode == "mudah":
        jumlah_tebakan_maks = 5
        rentang = (1, 20)
    elif mode == "sedang":
        jumlah_tebakan_maks = 4
        rentang = (1, 50)
    else:
        jumlah_tebakan_maks = 3
        rentang = (1, 100)

    angka_acak = random.randint (rentang[0], rentang[1])
    jumlah_tebakan_sisa = jumlah_tebakan_maks

    print(f"tebak angka antara {rentang[0]} dan {rentang[1]}. kamu punya {jumlah_tebakan_maks} kesempatan.")

    while jumlah_tebakan_sisa > 0:
        tebakan = int(input("masukan tebakanmu : "))
        jumlah_tebakan_sisa -= 1

        if tebakan == angka_acak:
            print("selamat, kamu berhasil!!!")
            break
        elif tebakan < angka_acak:
            print("telalu rendah")
        else:
            print("terlalu tinggi")

        print(f"sisa kesempatan: {jumlah_tebakan_sisa}")

    if jumlah_tebakan_sisa == 0:
        print(f"kesempatan habis. angka yang benar adalah {angka_acak}.")

if __name__ == "__main__":
    tebak_angka()

