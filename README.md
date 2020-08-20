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

```
sudo docker-compose up --build
```

## Executando os testes

- Alterar a variável de ambiente chamado ***ENV*** dentro do arquivo ```docker-compose.yml``` de ***dev*** para ***test***;
- ```sudo docker-compose up``` para rodar a aplicação;
- ```docker ps``` para obter ***id*** do container da aplicação principal;
- ```docker exec -it <container_id> bash``` para executar o bash e "entrar" no container da aplicação principal;
- ```python -m unittes``` para executar os testes.

## Acessando as funcionalidades da aplicação

#### Adicionar um planeta (com nome, clima e terreno)

POST: localhost:4000/planet
 - body: { "name" : "xxx", "cliamte" : "yyyyy", "terrain" : "zzzzzz" }

#### Listar planetas

GET: localhost:4000/planet

#### Buscar por nome;

GET: localhost:4000/planet/name/:planet_name

#### Buscar por ID;

GET: localhost:4000/planet/id/:planet_id

#### Atualizar planeta

DELETE: localhost:4000/planet
 - query: ```name=planet_name```
 - body: o(s) campo(s) que deseja atualizar(JSON)

#### Remover planeta

DELETE: localhost:4000/planet
 - query: ```name=planet_name```
