import re
import requests

est = requests.get('https://www.youtube.com/watch?v=sbTVZMJ9Z2I')

ern = re.findall(r'part: ', est.text)

if ern:
    print(ern)
else:
    print('Padrão não encontrado')

# regex101.com