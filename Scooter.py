def Maandkosten():
    km_per_maand = ""
    bezine_kosten_per_liter = ""
    verzekering_per_maand = ""
    liter_per_kilometer = ""
    
    while not isinstance(bezine_kosten_per_liter, float):

        try:
        #vragen om de input#
            bezine_kosten_per_liter = input("Voer bezine kosten per liter: ")

        #input omzetten naar een float#
            bezine_kosten_per_liter = float(bezine_kosten_per_liter)

        except ValueError:
            print(bezine_kosten_per_liter + " is geen geldig getal!")

    while not isinstance(liter_per_kilometer, float):

        try:
        #vragen om de input#
            liter_per_kilometer = input("voer liter per kilometer: ")

        #input omzetten naar een float#
            liter_per_kilometer = float(liter_per_kilometer)

        except ValueError:
            print(liter_per_kilometer + " is geen geldig getal!")

while not isinstance(verzekering_per_maand, float):

        try:
        #vragen om de input#
            verzekering_per_maand = input("voer verzekering per maand: ")

        #input omzetten naar een float#
            verzekering_per_maand = float(verzekering_per_maand)

        except ValueError:
            print(verzekering_per_maand + " is geen geldig getal!")

    while not isinstance(km_per_maand, float):

        try:
        #vragen om de input#
            km_per_maand = input("voer km per maand: ")

        #input omzetten naar een float#
            km_per_maand = float(km_per_maand)

        except ValueError:
            print(km_per_maand + " is geen geldig getal!")

    print(bezine_kosten_per_liter * liter_per_kilometer * km_per_maand + verzekering_per_maand)

print(Maandkosten())
.
.
.
dit is code van schooter
scooter