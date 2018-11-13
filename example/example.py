from turkishsuffix import turkishSuffix

print("Merhaba, hoş geldiniz, {} ulaşmak için {} aramak isterseniz {} telefon numarasını size verebiliriz."
      "İster miydiniz?".format(turkishSuffix.suffix("Bora", "yönelme", True).suffixed,
                               turkishSuffix.suffix("Bora", "belirtme", True).suffixed,
                               turkishSuffix.suffix("Bora", "ilgi", True).suffixed))

liste = "Muhittin", "Abdullah", "Bora", "Eyşan", "Ayşe", "Kamuran", "Fatma", "Kezban", "Burçin", "Rüya", "Umut",\
        "Umutcan", "Su", "Ne", "Kitap", "Elif", "Karargah", "Ağaç", "Kaltak", "Dut", "Fas", "Fiş", "Tren", "Hayal",\
        "General", "İntegral", "Kefal", "Legal", "Tarzan", "Şanzelize"


for item in liste:
    print(turkishSuffix.suffix(item, "iyelik", False, "1t"))
    print(turkishSuffix.suffix(item, "iyelik", False, "2t"))
    print(turkishSuffix.suffix(item, "iyelik", False, "3t"))
    print(turkishSuffix.suffix(item, "iyelik", False, "1ç"))
    print(turkishSuffix.suffix(item, "iyelik", False, "2ç"))
    print(turkishSuffix.suffix(item, "iyelik", False, "3ç"))
    print(turkishSuffix.suffix(item, "çokluk"))
    print(turkishSuffix.suffix(item, "ilgi", True))
    print(turkishSuffix.suffix(item, "eşitlik"))
    print(turkishSuffix.suffix(item, "yönelme"))
    print(turkishSuffix.suffix(item, "belirtme"))
    print(turkishSuffix.suffix(item, "bulunma"))
    print(turkishSuffix.suffix(item, "ayrılma"))
