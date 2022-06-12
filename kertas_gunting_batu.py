#Sun Jun 12 11:40:52 WIB 2022


# Masukan pilihan user (1.kertas, 2.gunting, 3.batu)
# Masukan pilihan komputer (acak 1-3)
# jika user pilih 1.kertas MAKA jika komputer pilih 2.gunting (Kamu kalah) dan sebaliknya kamu menang
# jika user pilih 2.gunting MAKA jika komputer pilih 1.kertas (Kamu menang) dan sebaliknya kamu kalah
# jika user pilih 3.batu MAKA jika komputer pilih 1.kertas (Kamu kalah) dan sebaliknya kamu menang
# jika pilihan kamu dan komputer sama maka draw
# JIKA user menang 3X maka point 100, jika 2X maka point 50, jika menang 1X maka point 25, jika tidak menang 3X maka kalah

score_user_menang = 0
score_user_kalah = 0
score_draw = 0
i = 1
from random import randint
from time import sleep
print('Simpel program\n1.Kertas, 2.Gunting, 3.Batu')
while i <= 3:
    pilih_user = int(input('\nMasukan pilihanmu: '))
    pilihan_comp = randint(1,3)

    if pilih_user == pilihan_comp: #Kondisi diawal
        print(f'Kamu:{pilih_user} VS Komputer:{pilihan_comp} = Draw !!!')
        score_draw += 1
        i+=1 #karema kalau di ignore bakal looping 4x
        continue #biar balik lagi ke looping

    if pilih_user == 1:
        if pilihan_comp == 2:
            print(f'Kamu:{pilih_user} VS Komputer:{pilihan_comp} = Kamu kalah!')
            score_user_kalah += 1
        else:
            print(f'Kamu:{pilih_user} VS Komputer:{pilihan_comp} = Kamu Menang!')
            score_user_menang += 1

    if pilih_user == 2:
        if pilihan_comp == 1:
            print(f'Kamu:{pilih_user} VS Komputer:{pilihan_comp} = Kamu Menang!')
            score_user_menang += 1
        else: 
            print(f'Kamu:{pilih_user} VS Komputer:{pilihan_comp} = Kamu kalah!')
            score_user_kalah += 1

    if pilih_user == 3:
        if pilihan_comp == 1:
            print(f'Kamu:{pilih_user} VS Komputer:{pilihan_comp} = Kamu kalah!')
            score_user_kalah += 1
        else:
            print(f'Kamu:{pilih_user} VS Komputer:{pilihan_comp} = Kamu Menang!')
            score_user_menang += 1

    i = i+1
sleep(1)
print(f"""
Menang = {score_user_menang}
Kalah = {score_user_kalah}
Draw = {score_draw}
""")
