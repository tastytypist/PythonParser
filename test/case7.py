# ALGORITMA
with open("fa.py") as fa:
    pass

N=int(input("Masukkan angka:"))
J=[]

if(N<2):
    print(str(N),"bukan bilangan prima")
else:
    for i in range(1,N**5+1):
        if(N%i==0):
            J=J[1:3]
    else:
        if(J>1):
            print(N,"bukan bilangan prima")
        else:
            print(N,"adalah bilangan prima")