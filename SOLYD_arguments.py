import sys

args = sys.argv

def soma(x, y):
    return x + y

def sub(x, y):
    return x - y

if (len(args) != 4):
    n = "PROBLEMA NA INSERÇÃO DO COMANDO"
elif args[1] == 'soma':
    n = soma(float(args[2]), float(args[3]))
elif args[1] == 'sub':
    n = sub(float(args[2]), float(args[3]))
else:
    n = "APENAS OS COMANDOS 'sub' E 'soma' SÃO SUPORTADOS"

print(n)
