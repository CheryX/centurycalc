print ("Welcome to my first ever code on github, enter year here.")
print ("NOTE: This only works for 4-digit years!")
year = int(input("> "))
print ("Now choose if you prefer B.C or A.D (B.C = 0, A.D = 1)")
era = int(input("> "))
year2 = int(str(year)[:2])
mil = int(str(year)[0])
half = int(str(year)[2:])
last3 = int(str(year)[:3])
if (era == 1):
    if (half == 00):
        century = year2
    else:
        century = year2 + 1
    if (half > 50) or (half == 0):
        halffc = 2
    else:
        halffc = 1
    if (last3 == 000):
        mil2 = mil
    else:
        mil2 = mil + 1
    if (last3 > 500) or (last3 == 000):
        hmil = 2
    else:
        hmil = 1
    print ("#################")
    print ("Year:", year)
    print ("#################")
    print ("Century:", century)
    print ("Half of Century:", halffc)
    print ("Millennium:", mil2)
    print ("Half of Millennium:", hmil)
    print ("#################")
else:
    if (half == 00):
        century = year2
    else:
        century = year2 + 1
    if (half > 50) or (half == 0):
        halffc = 1
    else:
        halffc = 2
    if (last3 == 000):
        mil2 = mil
    else:
        mil2 = mil + 1
    if (last3 > 500) or (last3 == 000):
        hmil = 1
    else:
        hmil = 2
    print ("#################")
    print ("Year:", year, "p.n.e")
    print ("#################")
    print ("Century:", century, "p.n.e")
    print ("Half of Century:", halffc, "p.n.e")
    print ("Millennium:", mil2, "p.n.e")
    print ("Half of Millennium:", hmil, "p.n.e")
    print ("#################")