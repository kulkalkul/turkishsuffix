from turkishsuffix import TurkishSuffix
name = TurkishSuffix("Bora")

print("Merhaba, hoş geldiniz, {} ulaşmak için {} aramak isterseniz {} telefon numarasını size verebiliriz. İster miydiniz?".format(name.get_word("yönelme", True), name.get_word("belirtme", True), name.get_word("ilgi", True)))

liste = "Muhittin", "Abdullah", "Bora", "Eyşan", "Ayşe", "Kamuran", "Fatma", "Kezban", "Burçin", "Rüya", "Umut", "Umutcan", "Su", "Ne", "Kitap", "Elif", "Karargah", "Ağaç", "Kaltak", "Dut", "Fas", "Fiş", "Tren"


for item in liste:
    iyelik = TurkishSuffix(item)
    print(iyelik.get_word("iyelik", False, "1t"))
    print(iyelik.get_word("iyelik", False, "2t"))
    print(iyelik.get_word("iyelik", False, "3t"))
    print(iyelik.get_word("iyelik", False, "1ç"))
    print(iyelik.get_word("iyelik", False, "2ç"))
    print(iyelik.get_word("iyelik", False, "3ç"))
    print(iyelik.get_word("çokluk"))
    print(iyelik.get_word("ilgi", True))
    print(iyelik.get_word("eşitlik"))
    print(iyelik.get_word("yönelme"))
    print(iyelik.get_word("belirtme"))
    print(iyelik.get_word("bulunma"))
    print(iyelik.get_word("ayrılma"))
    print(iyelik.get_word())
