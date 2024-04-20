import requests
import json

def req(title):
    est = requests.get('http://www.omdbapi.com/?apikey=2dd4326c&t=' + title + '&type=movie')
    ary = json.loads(est.text)
    return ary
    
def data(moviedata):
    if moviedata['Response'] == 'False': print('Esse filme não existe!')
    else:
        print('Título: ', moviedata['Title'])
        print('Ano: ', moviedata['Year'])
        print('Gênero: ', moviedata['Genre'])
        print('Prêmios: ', moviedata['Awards'])
        print('Nota IMDB: ', moviedata['imdbRating'])
        print('Orçamento: ', moviedata['BoxOffice'])

while True:
    wer = input('Escreva o nome do filme para saber seus dados, ou SAIR para fechar o programa: ')
    if wer == 'SAIR': break
    else: data(req(wer))
