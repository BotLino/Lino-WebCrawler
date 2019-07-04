# Lino-WebCrawler

<a href="https://codeclimate.com/github/BotLino/Lino-WebCrawler/maintainability"><img src="https://api.codeclimate.com/v1/badges/ec1c98cb93b2fe8c01c0/maintainability" /></a>

## Objetivo

Microsserviço feito com o objetivo de buscar o cardápio do RU e envia-lo para o Core (Lino)

## Como usar

### Pré requisitos
Instale o docker e o docker-compose, e rode o seguinte comando:
```
$ docker-compose -f docker-compose-dev.yml up --build
```

### Endpoints
### ```/cardapio/update```

Objetivo: Realiza o download do cardapio da semana e atualiza o banco de dados.

Verbo: ```GET```

| Parâmetros de entrada | Descrição |
| :-------------------: | :-------: |
| Nenhum                |


```200```: quando a requisição é feita com sucesso a api redireciona para a home.

### ```/cardapio/week```
Verbo: ```GET```

| Parâmetros de entrada | Tipo           | Descrição             |
| :-------------------: | :------------: | :-------------------: |
| ```nenhum```            |  |   |

```200```: Retorna um json com o cardápio completo da semana.

### ```/cardapio/<day>```
Verbo: ```GET```

| Parâmetros de entrada na URL | Tipo           | Descrição        |
| :--------------------------: | :------------: | :--------------: |
| ```day```                  | ``` string ``` | Dia da semana (em inglês) |


Exemplo: 

Parâmetro de entrada: ```Wednesday```

URL: localhost:3000/cardapio/**Wednesday**


| Saída       | Tipo           | Descrição        |
| :---------: | :------------: | :--------------: |
| ```ALMOÇO```  | ``` object ``` | Objeto com os conteúdos do almoço do dia  |
| ```JANTAR```  | ``` object ``` | Objeto com os conteúdos do jantar do dia  |
| ```DESJEJUM```  | ``` object ``` | Objeto com os conteúdos do café da manhã do dia  |

### ```/cardapio/<day>/Almoco```
Verbo: ```GET```

| Parâmetros de entrada na URL | Tipo           | Descrição        |
| :--------------------------: | :------------: | :--------------: |
| ```day```                  | ``` string ``` | Dia da semana (em inglês) |


Exemplo: 

Parâmetro de entrada: ```Wednesday```

URL: localhost:3000/cardapio/**Wednesday**/Almoco


| Saída       | Tipo           | Descrição        |
| :---------: | :------------: | :--------------: |
| ```ALMOÇO```  | ``` object ``` | Objeto com os conteúdos do almoço do dia  |

### ```/cardapio/<day>/Jantar```
Verbo: ```GET```

| Parâmetros de entrada na URL | Tipo           | Descrição        |
| :--------------------------: | :------------: | :--------------: |
| ```day```                  | ``` string ``` | Dia da semana (em inglês) |


Exemplo: 

Parâmetro de entrada: ```Wednesday```

URL: localhost:3000/cardapio/**Wednesday**/Jantar


| Saída       | Tipo           | Descrição        |
| :---------: | :------------: | :--------------: |
| ```JANTAR```  | ``` object ``` | Objeto com os conteúdos do jantar do dia  |

### ```/cardapio/<day>/Desjejum```
Verbo: ```GET```

| Parâmetros de entrada na URL | Tipo           | Descrição        |
| :--------------------------: | :------------: | :--------------: |
| ```day```                  | ``` string ``` | Dia da semana (em inglês) |


Exemplo: 

Parâmetro de entrada: ```Wednesday```

URL: localhost:3000/cardapio/**Wednesday**/Desjejum


| Saída       | Tipo           | Descrição        |
| :---------: | :------------: | :--------------: |
| ```DESJEJUM```  | ``` object ``` | Objeto com os conteúdos do jantar do dia  |
