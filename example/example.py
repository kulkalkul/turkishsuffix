import turkishsuffix

users = "Muhittin", "Abdullah", "Bora", "Eyşan", "Ayşe", "Kamuran", "Fatma", "Kezban", "Burçin", "Rüya", "Umut", "Umutcan", "Su", "Ne", "Kitap", "Elif", "Karargah", "Ağaç", "Kaltak", "Dut", "Fas", "Fiş", "Tren"


for user in users:
    userSuffix = turkishsuffix.Suffix(user, "çokluk")
    print(userSuffix.get_word())
    userSuffix.set_suffix("ilgi")
    print(userSuffix.get_word(True))
    userSuffix.set_suffix("eşitlik")
    print(userSuffix.get_word(False))
    userSuffix.set_suffix("yönelme")
    print(userSuffix.get_word(True))
    userSuffix.set_suffix("belirtme")
    print(userSuffix.get_word())
    userSuffix.set_suffix("bulunma")
    print(userSuffix.get_word(True))
    userSuffix.set_suffix("ayrılma")
    print(userSuffix.get_word(False))

name = turkishsuffix.Suffix("Bora")

print("Merhaba, hoş geldiniz, {} ulaşmak için {} aramak isterseniz {} telefon numarasını size verebiliriz. İster miydiniz?".format(name.get_word(True, "yönelme"), name.get_word(True, "belirtme"), name.get_word(True, "ilgi")))
