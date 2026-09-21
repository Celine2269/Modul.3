# Feilsøking
navn = "Michael"
alder = 31

print("Hei, jeg heter", navn)
print("Jeg er", alder, "år gammel")
print("Ha det!")

# Refleksjon
# 1. Navn var ikke definert som en 'string', manglet hermetegn.
# Første print hadde en skrivefeil (pritn). Andre print manglet 
# hermetegn etter "år gammel. Siste print manglet parantes på slutten.
# 2. Ingen var vanskelige å finne, men tenkte ikke over navn=Michael 
# feilen før python påpekte det...
# 3. Feilmeldingen viste riktig linje, men startet på linje 6