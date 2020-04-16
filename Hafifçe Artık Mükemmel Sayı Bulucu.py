"""
Bu algoritma hafifçe artık mükemmel sayı bulmaya çalışır.

Hafifçe artık mükemmel sayı, bir sayı olacak ve o sayının kendisi harici bütün bölenlerinin
toplamı kendisinden bir fazla olan sayıdır. Bu sayı henüz bulunamamıştır fakat
böyle bir sayı bulunmadığı da kanıtlanamamıştır.

Mükemmel sayı, bir sayı olacak ve o sayıının kendisi hariç bütün bölenlerinin
toplamı sayının kendisine eşit olan sayılardır Örenek 6.

Hafifçe eksik mükemmel sayı, bir sayı olacak ve o sayının kendisi harici bütün bölenlerinin
toplamı kendisinden bir eksik olan sayıdır. bunlar 2 üzeri n olan bütün
sayılarda geçerlidir. Örnek 4 8 16 32 64.

Ben 700000 e kadar denedim bulamadım. Eğer isterseniz
sayi=0 olan yerdeki 0 yerine 700000 yazıp siz devam edebilirsiniz.
Sayı bulunduğunda "Bulundu" yazacaktır.

Sayılar büyüdükçe hesaplama işlemi yavaşlıyacaktır.

Dikkat:Yazılımı buradan F5 e basarak çalıştırın.

Kodlar bana aittir.
"""

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
