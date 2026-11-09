def scitano(a, b):
    return a + b

a = 5
b = 10
vysledek = scitano(a, b)
print("Výsledek sčítání:", vysledek)

def deleni(a, b):
    if b == 0:
        return "Chyba: Dělení nulou není povoleno."
    return a / b

vysledek_deleni = deleni(a, b)
print("Výsledek dělení:", vysledek_deleni)

def mocnina(a, b):
    return a ** b

vysledek_mocnina = mocnina(a, b)
print("Výsledek mocniny:", vysledek_mocnina)