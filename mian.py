nominaly = [
    50000,  # 500 zł
    20000,  # 200 zł
    10000,  # 100 zł
    5000,   # 50 zł
    2000,   # 20 zł
    1000,   # 10 zł
    500,    # 5 zł
    200,    # 2 zł
    100,    # 1 zł
    50,     # 50 gr
    20,     # 20 gr
    10,     # 10 gr
    5,      # 5 gr
    2,      # 2 gr
    1       # 1 gr
]

reszta = []

kwota = int(input("Podaj kwotę do wydania [wartość podaj w groszach]: "))

n = 0

while kwota > 0:
    print(f'---------------------{nominaly[n]/100}-zł---------------------')
    x = kwota//nominaly[n]
    print(f'Wydaj {x} razy')
    for i in range(1, x+1):
        reszta.append(nominaly[n])
    kwota = kwota - (nominaly[n]*x)
    print(f'Zostało {kwota/100} zł do wydania')
    n += 1

print("\n")

print(reszta)