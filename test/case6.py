# Algoritma
bilangan = int(input("Masukkan bilangan : "))
a = 0
for i in range(1,bilangan):
    if bilangan%i == 0:
        a = a + i # Di sini variabel a akan menampung penjumlahan dari faktor bilangan input
if a == bilangan: # Syarat bilangan sempurna adalah dimana jumlah dari faktor - faktornya sama dengan bilangan input
    print("Bilangan tersebut adalah bilangan sempurna.")
else:
    print("Bilangan tersebut bukan bilangan sempurna.")
