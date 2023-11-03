"""
Uzrakstiet programmu definējot klasi,lai veselu skaitli pārveidotu par romiešu ciparu.

1) Kādus ciparus Jūs ziniet?
- arābu no 0 līdz 9
2) Kādus Romiešu ciparus jūs zinie?
-I, V, X, C, L, D
3) Kas ir klase?
- Programmēšanas struktūra, kas var definēt datu uzvedību un metodes
4) klase sastāv no konstruktora vai destruktora un metodēm (iekšējām funkcijām)
5) Kādas datu struktūras ziniet?
- list (saraksts)
- arry (masīvs)
- dict (vārdnīca) a={} a=dict{}
vārdnīcu var saprast kā vārdnīcu ar divām kolonām
viena kolona ir atslēga un otra ir vērtība
Parametri () - iekšējie klases mainīgie

"""
class AAA:
    # jādefinē konstruktors
    def __init__(self):
        self.roma_sk={
            1:'I',
            4:'IV',
            5:'V',
            9:'IX',
            10:'X',
            40: 'XL', 
            50: 'L', 
            90: 'XC', 
            100: 'C', 
            400: 'CD', 
            500: 'D', 
            900: 'CM', 
            1000: 'M'
        }
    # definē nepieciešamās metodes
    def to_roman(self, num):
        result = ""
        for value, numeral in sorted(self.roma_sk.items(), key=lambda x: x[0], reverse=True):
            while num >=value:
                result += numeral
                num -=value
# piemērs
skaitlis=2023
#definējam objektu
kk=AAA()
# jaunajam objektam jāizsauc klases metode
romieshu=kk.to_roman(skaitlis)

# Noformēt izdruku
print(f"{skaitlis} ar romiešu cipariem ir {romieshu}")