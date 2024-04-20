# word = 'king of the kings'

# namelist = ['ana', 'beatriz', 'caio', 'davi', 'elise', 'felipe']

# i = 0

# while True:
#     print(i)
#     if i == 20:
#         break
#     i += 1

# print(i)

i = 0
guestlist = []

print("Custo dos Convidados")
print("Digite todos os covidados, e, após o término, digite '.':")

while i == 0:
    guest = input('')
    if guest == '.':
        break
    guestlist.append(guest)

print("Quanto é o gasto previsto por convidado (em reais)?")
cost = int(input(''))
totalcost = len(guestlist) * cost

print('Seus convidados são:')

for name in guestlist:
    print(name)

print('E o custo total será de', totalcost, ' reais.')