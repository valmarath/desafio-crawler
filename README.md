# Desafio crawler

Neste repositório encontra-se minha interpretação do [desafio de crawler](https://github.com/beemontech/desafio-crawler) proposto pela beeMôn.

Consegui realizar grande parte dos entregáveis do desafio, de acordo com minha interpretação, deixando pendente apenas a parte de dockerizar a aplicação e incluir a funcionalidade de agendamento de execução. 

### Antes de Rodar o desafio:
O arquivo principal onde foi realizado todo o desenvolvimento do desafio é o [crawler_gabriel_valmarath.py](https://github.com/valmarath/desafio-crawler/blob/main/venv/crawler_gabriel_valmarath.py)

Para que seja possível testar a aplicação, as seguintes `bibliotecas` deverão ser instaladas de antemão:

- Requests
- BeautifulSoup
- Pandas
- Pymongo
- Json
- Selenium
- Pillow

Também é importante que o [mongoDB](https://www.mongodb.com/docs/v5.0/tutorial/install-mongodb-on-windows/) esteja instalado no momento de testar a aplicação. O código foi feito utilizando a versão 5.0 do mongoDB, logo, recomenda-se que a mesma seja [instalada](https://www.mongodb.com/docs/v5.0/tutorial/install-mongodb-on-windows/).

Com o mongoDB instalado, deve-se iniciar o mesmo antes de rodar a aplicação. Para o sistema operacional Windows, o processo recomendado é de abrir via terminal ou prompt de comando e então inserir o código abaixo:
  ```bash
  $ cd <caminho até a pasta bin mongodb> 
  $ # cd C:\Program Files\MongoDB\Server\5.0\bin, por exemplo
  $ mongod.exe
  ``` 
 É necessário manter o terminal aberto com o mongo rodando para que a execução do crawler tenha êxito em inserir os resultados no banco de dados.
 
### Para testar o resultado:

Para testar os resultados efetivamente, basta executar o arquivo via interface do seu editor de código, ou pelo terminal, através do comando `python crawler_gabriel_valmarath.py`.

Os resultados esperados,  conforme descritos nos entregáveis do desafio original, irão aparecer no console do editor de código. Também será criado um arquivo chamado `consulta.png`, o qual diz respeito a prova de consulta solicitada. Será criado, conjuntamente, um arquivo chamado `imdbMovies.csv` com os resultados do crawling. Os mesmos dados serão inseridos no seu banco de dados `mongoDB` (database: desafioCrawler, collection: imdbMovies).

