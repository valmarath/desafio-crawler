import requests
from bs4 import BeautifulSoup
import pandas as pd
from pymongo import MongoClient
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from PIL import Image
#import schedule
#import time

#url do imdb, link escolhido dentre as duas opções para executaro crawler
url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

def main():
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")

    # Tabela contendo todos os filmes
    masterTable = soup.find('tbody', {"class": "lister-list"})

    # Lista de filmes
    movieList = masterTable.find_all('tr')

    #Criando array para posterior inserção no dataframe (pandas)
    data= []

    # Iterando na lista de filmes para pegar informações
    for movieItem in movieList:
        movieItemInfo = movieItem.find_all('td')
        movieItemArray = movieItemInfo[1].text.split("\n")
        movieRank = movieItemArray[1].replace(' ','').replace('.', '')
        print("Posição no Rank:", movieRank)
        movieTitle = movieItemArray[2].strip()
        print("Título do Filme:", movieTitle)
        movieDate = movieItemArray[3].replace('(','').replace(')','')
        print("Data:", movieDate)
        movieRating = movieItemInfo[2].text.split("\n")[1]
        print("Nota do IMDb:", movieRating)
        print("\n")
        data.append([movieRank, movieTitle, movieDate, movieRating])

    # Criando dataframe
    df = pd.DataFrame(data, columns=['movieRank', 'movieTitle', 'movieDate', 'movieRating'])
    print(df)

    # Gerando CSV e JSON com resultados
    df.to_csv("imdbMovies.csv", index=False)
    print('Resultado em csv salvo com sucesso!')
    dfJson = df.to_json(orient = "records")
    print(dfJson)


    # Armazenando resultados no mongoDB
    URI = "mongodb://localhost:27017/myDB"
    client = MongoClient(URI)
    db = client.desafioCrawler
    imdbMovies = db.imdbMovies

    #Caso queira rodar o script novamente e já tenha inserido os dados uma vez no banco, remover o '#' da linha abaixo para
    #não duplicar os mesmos
    #imdbMovies.drop()

    imdbMovies.insert_many(json.loads(dfJson))


    # Prova de consulta
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    el = driver.find_element(By.TAG_NAME, "body")
    total_height = el.size["height"] + 1000
    driver.set_window_size(1920, total_height)
    el.screenshot("consulta.png")
    print('Prova de consulta salva com sucesso!')
    driver.quit()

if __name__ == '__main__':
    main()


#Tentativa de agendamento de execução do crawler, não funcionou

# daySchedule = ''
# timeSchedule = ''
#
# schedule.every().wednesday.at("01:36").do(main)
#
# while True:
#     user_input = input('Gostaria de rodar o crawler agora ou agendar? Respostas possíveis: agora / agendar \n')
#     print(user_input)
#     if user_input == 'agora':
#         main()
#     elif user_input == 'agendar':
#         user_input2 = input('Qual dia da semana você gostaria de executar o crawler? Respostas possíveis: segunda / '
#                             'terca / quarta / quinta / sexta / sabado / domingo \n')
#         if user_input2 == 'segunda':
#             daySchedule = 'monday'
#         if user_input2 == 'terca':
#             daySchedule = 'tuesday'
#         if user_input2 == 'quarta':
#             daySchedule = 'wednesday'
#         if user_input2 == 'quinta':
#             daySchedule = 'thursday'
#         if user_input2 == 'sexta':
#             daySchedule = 'friday'
#         if user_input2 == 'sabado':
#             daySchedule = 'saturday'
#         if user_input2 == 'domingo':
#             daySchedule = 'sunday'
#         user_input3 = input('Qual horário você gostaria de executar o crawler? Exemplo: 13:15 \n')
#         timeSchedule = user_input3
#     else:
#         print('Parar crawler')
#         break
#     schedule.run_pending()
#     time.sleep(30)


