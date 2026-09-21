# Variabler
brus = 24.90
smørbrød = 45
banan = 8.50

totalsum = brus + smørbrød + banan  # Mindre skriving i oppgaver

# Print
print("Totalsum:", totalsum, "kr")
print ("Totalsum med 25% mva:", totalsum * 1.25, "kr")
print("Pris per person (4 personer):", totalsum / 4, "kr")
print("Prisforskjell mellom dyreste og billigste vare:", smørbrød - banan, "kr")

# Refleksjon
# 1. Summen ble en 'float', et desimaltall.
# 2. Ble en 'float', ikke overrasket.
# 3. Hvis prisen stiger på èn eller flere varer kan man endre
# kun tallene i variablene, og summene oppdateres. Mindre jobb :)