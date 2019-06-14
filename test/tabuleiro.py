posicoes = [0,0,0,0,0,0,0,0,0]

divisor = '---------------------'

for x in range(len(posicoes)):
    if x%3 == 0:
        print("\n" + divisor)
    if posicoes[x] == -1:
        print(f'|  X  |', end='')
    elif posicoes[x] == 1:
        print(f'|  O  |', end='')
    else:
        print(f'|     |', end='')
print("\n" + divisor)