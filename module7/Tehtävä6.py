import math
def pizzan_yksikköhinta(halkaisija:float, hinta:float):
    yksikköhinta = hinta / ((halkaisija / 2) ** 2 * math.pi)
    return yksikköhinta

pizza1_halkaisija = float(input("Anna ensimmäisen pizzan halkaisija: "))
pizza1_hinta = float(input("Anna ensimmäisenj pizzan hinta: "))
pizza2_halkaisija = float(input("Anna toisen pizzan halkaisija: "))
pizza2_hinta = float(input("Anna toisen pizzan hinta: "))

pizza1_yksikköhinta = pizzan_yksikköhinta(pizza1_halkaisija, pizza1_hinta)
pizza2_yksikköhinta = pizzan_yksikköhinta(pizza2_halkaisija, pizza2_hinta)

if pizza1_yksikköhinta < pizza2_yksikköhinta:
    print(f"Ensimmäinen pizza antaa paremman vastineen rahalle.")
elif pizza1_yksikköhinta > pizza2_yksikköhinta:
    print(f"Toinen pizza antaa paremman vastineen rahalle.")
else:
    print(f"Molemmat pizzat antavat saman vastineen rahalle.")