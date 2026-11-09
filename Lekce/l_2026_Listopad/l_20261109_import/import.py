import math

print(f"Číslo PI: {math.pi}")
print(f"sinus 90 stupnu: {math.sin(math.pi / 2)}")

def bezpecne_deleni(a, b):
    try:
        vysledek = a / b
    except ZeroDivisionError as zde:
        print(f"Chyba: {zde}")
        return None
    except Exception as e:
        zprava = f"nelze delit objekt: {a} / {b}: {e}"
        raise Exception(zprava)
    finally:
        print("Dělení bylo provedeno.")
        print("tento blok se provede vždy")
    return vysledek

print(bezpecne_deleni(10, 2))
print(bezpecne_deleni(10, 0))