spin_ekrani=[[1,1,3],
             [1,1,2],
             [1,1,1]
]

ayni_satir=0

for satir in spin_ekrani:
    if all(satir[0]==eleman for eleman in satir):
        ayni_satir += 1

print(ayni_satir)