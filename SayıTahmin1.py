import random
x = random.randint(1,100)
score = 100

print("Merhaba! Bu oyunda görevin rastgele belirlemiş 1 ila 100 arasındaki sayıyı tahmin etmek.")
print("Sayıyı kaç tahminde bileceğini soracağız")
print("ve her yanlış tahminde seni aşağı yada yukarı ile seni doğru sayıya yönlendireceğiz.")
print("Toplam tahmin sayısı ile kullandığın tahmin sayısı puanını belirleyecek.")
attempt = 0
while attempt <= 0 or attempt > 20:
    attempt = int(input("Kaç tahminde bulunacaksın? "))
    if attempt <= 0 or attempt > 20:
            print("Hak sayısı Negatif , sıfır yada 20'den fazla tanımlanamaz.")
            continue
    else:
        print("Pekala. Başlayalım.")
        pointloss = 100/attempt
        break

pointloss = 100/attempt

while not attempt == 0:
    answer = int(input("tahmininiz: "))
    if answer == x:
        print("tebrikler! cevap doğru")
        print ("***")
        print(f"puanınız: {score} / 100")
        break
    elif answer < x:
        score -= pointloss
        attempt-= 1
        if score == 0 or attempt == 0:
            print(f"Deneme hakkınız bitti. Kaybettiniz. Doğru cevap {x} idi")
            break
        else:
            print ("---")
            print ("Yukarı")
            print(f"kalan tahmin hakkınız: {attempt} puan: {score}")
            print ("---")
        continue
    elif answer > x:
        score -= pointloss
        attempt-= 1
        if score == 0 or attempt == 0:
            print(f"Kaybettiniz. Doğru cevap {x}.")
            break
        else:
            print ("---")
            print ("Aşağı")
            print(f"kalan hak: {attempt} puan: {score}")
            print ("---")
        continue

print(input("Çıkmak için bir tuşa basınız."))
