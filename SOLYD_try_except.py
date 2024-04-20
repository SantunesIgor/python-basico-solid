# try: a = asd()
# except ZeroDivisionError: 
#   print('Impossibilidade matemática - Divisão por 0')
# except NameError: 
#   print('Valor não suportado')

# try: 
#     asdasd()
# except Exception as error:
#     print(error)

import time

def openfile():
    try:
        file = openfile('errorfile.txt')
        return file
    except:
        return False