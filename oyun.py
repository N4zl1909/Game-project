import random
bilgisayar=random.choice(["taş","kagit","makas"])
kullanıcı=input("taş,kagit ya da makas yaz:")
bilgisayar = random.choice(["taş", "kağıt", "makas"])
kullanıcı = input("taş, kağıt ya da makas yaz: ").lower()
print("Bilgisayarın seçimi:", bilgisayar)

if kullanıcı == bilgisayar:
    print("Berabere")
elif kullanıcı == "taş" and bilgisayar == "kağıt":
    print("Kaybettin")
elif kullanıcı == "makas" and bilgisayar == "taş":
    print("Kaybettin")
elif kullanıcı == "taş" and bilgisayar == "makas":
    print("Kazandın")
elif kullanıcı == "makas" and bilgisayar == "kağıt":
    print("Kazandın")
elif kullanıcı == "kağıt" and bilgisayar == "taş":
    print("Kazandın")
elif kullanıcı == "kağıt" and bilgisayar == "makas":
    print("Kaybettin")
else:
    print("Geçersiz seçim yaptın! Lütfen 'taş', 'kağıt' veya 'makas' yazınız.")
print("Oyun bitti")