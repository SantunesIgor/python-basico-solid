# print("Opções:\n1 - Vai para cima\n2 - Vai à esquerda\n3 - Vai para baixo\n4 - Vai à direita")
# ans = input()

# if ans == str(1):
#     print("Você foi para cima")
# elif ans == str(2):
#     print("Você foi para à esquerda")
# elif ans == str(3):
#     print("Você foi para baixo")
# elif ans == str(4):
#     print("Você foi à direita")
# else:
#     print("Não há nada aqui...")

print("Teste do Exército Brasileiro")
i = input("Qual a sua idade (apenas o número em anos): ")
p = input("Qual a seu peso (apenas o número em kg): ")
h = input("Qual a sua altura (apenas o número em cm): ")

if i <= str(18):
    print("Você é muito novo para servir ao Exército")

if p <= str(60):
    print("Você não tem peso suficiente para servir ao Exercíto")

if h <= str(170):
    print("Você é muito baixo para servir ao Exército")

if i >= str(18) and p >= str(60) and h >= str(170):
    print("Você pode servir ao Exército!")