##Dikkat:Yazılımı buradan F5 e basarak çalıştırın.
sayi=0
tambolenler = []
toplam=0
sayac=0
dongu=1
while dongu:

    tambolenler = []
    toplam=0

    for h in range (1,sayi):
        if(sayi%h==0):
            tambolenler.append(h)
            toplam+=h
            sayac+=1
            tumu=[tambolenler,toplam,sayac]
    print(
        "sayı={} ,toplam={},bölenler={} ".format(
            sayi, toplam, tambolenler))
    if toplam-1==sayi:
        dongu=0
        print("bulundu")
    anahtar=1
    while anahtar:
        sayi+=1
        for i in range(2,sayi):
            if(sayi%i==0):
                anahtar=0
