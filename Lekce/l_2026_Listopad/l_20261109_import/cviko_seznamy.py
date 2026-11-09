import math
Jmeno = "Petr"
Vek = 30
print(f"Jmeno: {Jmeno}, Vek: {Vek}")
numbers = [1, 2, 3, 4, 5]

numbers.append(6)
numbers.sort()
print(f"Seznam cisel: {numbers}")
print(f"prvni cislo: {numbers[0]}")
print(f"posledni cislo: {numbers[-1]}")
#slovniky, mnoziny

student = {
    "vek": 30,
    "jmeno": "Matěj",
    "predmety": ["Matematika", "Český Jazyk", "Informatika"]
}

student ["vek"] = 25
student ["jmeno"] = "Petr"
student ["predmety"] = ["Matematika", "Fyzika", "Informatika"]
print(f"Student: {student}")

data = [3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
unique_data = set(data)
print(f"Unikatni data: {unique_data}")

for i in range(1, 11):
    if i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

def vypocet_obvodu_obdelniku(delka, sirka = None):
    if sirka is None:
        sirka = delka
    return 2 * (delka + sirka)
delka = 5
sirka = 10

print(f"Obvod obdelniku: {vypocet_obvodu_obdelniku(delka, sirka)}")

odmocnina = math.sqrt(256)
print(f"Odmocnina z 256 je: {odmocnina}")

print(dir(math))