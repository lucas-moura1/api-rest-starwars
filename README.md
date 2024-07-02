![STARWARS](docs/star-wars-logo.png?raw=true "Logo STARWARS")

# api-rest-StarWars-Flask

Este repositório contém uma API REST em Node.js que contenha os dados dos planetas que são obtidos através do banco de dados MongoDB da aplicação, sendo inserido manualmente: Nome, Clima, Terreno.

Funcionalidades da Aplicação:
 - Adicionar um planeta (name, climate e terrain);
 - Listar planetas;
 - Atualizar os dados de planeta;
 - Buscar por nome;
 - Buscar por ID;
 - Remover planeta.

## Executando a aplicação

É necessário ter o ***docker*** e o ***docker-compose*** instalado na máquina local e executar o seguinte comando no terminal dentro da pasta do repositório:

```bash
docker compose up
```

## Executando os testes

- Alterar a variável de ambiente chamado ***ENV*** dentro do arquivo ```docker-compose.yml``` de ***dev*** para ***test***;
- ```docker compose up``` para rodar a aplicação;
- ```pytest``` para executar os testes.

## Acessando as funcionalidades da aplicação

#### Adicionar um planeta (com nome, clima e terreno)

POST: localhost:8000/planets
 - body:
```json
{ "name" : "xxx", "cliamte" : "yyyyy", "terrain" : "zzzzzz" }
```

#### Listar planetas

GET: localhost:8000/planets

#### Buscar por nome;

GET: localhost:8000/planets/:planet_name

#### Atualizar planeta

PUT: localhost:8000/planets/:planet_name
 - body:
```json
{"cliamte" : "yyyyy", "terrain" : "zzzzzz", "count_films": 3 }
```

#### Remover planeta

DELETE: localhost:8000/planets/:planet_name
