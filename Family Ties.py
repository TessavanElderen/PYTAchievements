naam = str("Hallo, Mijn naar is Tessa en ik ben {} jaar oud,")
leeftijd = int(19)
woonplaats = str("Ik woon in Naarden en dat is {} kilometer van het MediaCollege Amsterdam")
afstand = int(25.8)
hobby = str("Ik hou erg veel van astronomie, I love It! Ik ben er meer dan {} jaar in geïnteresseerd in.")
hobbytijd = int(5)
familie = str("Ik ben heel erg gehegd aan mijn familie. Ik vind daarom respect voor een ander heel erg belagrijk, want dat heb ik ook in mijn eigenlijk familie.")

print(naam.format(leeftijd) + woonplaats.format(afstand) + hobby.format(hobbytijd) + familie)
