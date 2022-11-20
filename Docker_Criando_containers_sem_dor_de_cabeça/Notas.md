# Aula 02 - Trabalhando com imagens

## Capitulo 01 - Comandos básicos com containers

Em linhas gerais, `docker` roda o docker quando utilizamos algum argumento adicionar

`docker version`: Exibe a versão do docker instalada.

`docker run (imagename)`: O docker roda uma imagem. Caso não tal imagem não exista localmente, o docker baixa tal imagem, cria e starta o container a partir da imagem.

`docker ps`: lista todos os containers ativos
`docker ps -a`: lista todos os containers criados, mesmo não ativos

|CONTAINER ID|   IMAGE|               COMMAND|                  CREATED|          STATUS|                      PORTS|                NAMES|
|-|-|-|-|-|-|-|
|e4c5467e7035|   ubuntu|              "bash"|                   33 seconds ago|   Exited (0) 31 seconds ago||                        blissful_khorana|
|a7cfa79cce65|   hello-world|         "/hello"|                 6 minutes ago  |  Exited (0) 6 minutes ago| |                        trusting_bohr|
|c49a61e2a037|   docker101tutorial   |"/docker-entrypoint.…"|   2 hours ago|      Up 2 hours                  |0.0.0.0:80->80/tcp|   docker-tutorial|
|b05f42f02962 |  alpine/git|          "git clone https://g…"|   2 hours ago      |Exited (0) 2 hours ago||                           repo|

### Um exemplo:
Ao utilizar `docker run ubuntu`, como comentamos acima, existe todo um processo por trás da criação de um container com a imagem do ubuntu. Porém, este comando não nos retorna nada, apenas faz com que o container seja executado.

Porém, podemos executar comandos dentro deste container, passando tal comando juntamente com o `docker run (comando a ser executado)`, como, por exemplo `docker run ubuntu echo "Hello World"``
```
PS C:\Users\Jefferson Amorim> docker run ubuntu echo "Hello World"
Hello World
```

Porém, temos um problema com o que foi feito acima: Toda vez que executarmos `docker run ubuntu <comando>` o docker vai gerar um novo container do ubuntu e exectuar aquele comando nele. Para resolver este problema, temos, podemos associar o **cmd** que estamos utilizando com o **cmd** do container em questão. Para isso, utilizarmos o argumento `-it` ao rodar o docker
```
docker run -it ubuntu
```
Feito isso, poder utilizar, por exemplo, `apt-get update` diretamente através do terminal.

### Reinicializando um container e ligando o cmd à ele.

O comando `docker start <idcontainer>` inicializa o container com aquele id, enquanto o comando `docker stop <idcontainer>` encerra tal container.

Uma vez startado, podemos associar nosso àquele container diretamente quando o começamos utlizando o comando
```
docker start -a -i <idcontainer>
```

## Capítulo 02 - Layered File System

Como vimos anteriormente, toda vez que rodamos o comando `docker run <container>`, um novo container é criado e executado. O próximo passo é aprendermos a excluir e limpar containers.

O primeiro comando é o `docker rm <idcontainer>`, que remove o container com aquele dado id. Vale a pena notar aqui que não precisamos passar o id completo do container, caso ele seja o único com um aquela string, o docker é esperto e remove, por exemplo: `docker rm e4c` vai remover o container com id `e4c5467e7035`, caso `e4c` seja o suficiente para identificá-lo.

Agora, caso seja do nosso interesse remover vários containers inativos de uma só ver, podemos utilizar o comando
```
docker container prune
```

## Capítulo 05 - Praticando com o docker run

Agora, vamos criar um container um pouco mais complexo.
Vamos utilizar o
```
  docker run dockersamples/static-site
```
Porém, quando inicializamos este container, nosso terminal fica 'preso' neste processo. Para rodá-lo de maneira independente ao terminal, rodá-lo no background, utilizamos o argumento `-d` de 'Detached'.

Além disso, precisamos ainda utilizar o argumento `-P` para que o docker associe as portas utilizadas no container à portas do computador de maneira automática e assim, possamos acessar o nosso site.
(Vale a pena notar que podemos também usar o argumento `-p` para escolheremos qual porta será associada `-p 12345:80`)
```
PS C:\Users\Jefferson Amorim> docker run -d -P dockersamples/static-site
eaa935600f2bda28c8805f376390d4747a9e6e8167f48e7717396bdc2d98cdf4
PS C:\Users\Jefferson Amorim> docker ps
CONTAINER ID   IMAGE                       COMMAND                  CREATED         STATUS         PORTS                                           NAMES
eaa935600f2b   dockersamples/static-site   "/bin/sh -c 'cd /usr…"   9 seconds ago   Up 6 seconds   0.0.0.0:49158->80/tcp, 0.0.0.0:49157->443/tcp   festive_johnson
PS C:\Users\Jefferson Amorim>

```

Feito isso, podemos acessar esta pagina utlizando o endereço `http://localhost:49158` onde **49158** indica a porta 80 que foi associada à este container.

### Dando nome aos containers
Todas as ações que realizamos com nossos containers,foram a partir de seus ids, gerados pelo proprio docker e, a medida que o tempo passa, lembrar quais são estes ids pode ser uma tarefa complicada. Para isso, podemos dar nomes aos containers ao criá-los para assim, facilitar nossa vida. Isto é feito utilizando o parametro `--name <nomedocontainer>`
```
PS C:\Users\Jefferson Amorim> docker run -d -P --name meusite dockersamples/static-site
ca9c4e0336fa1ee03485f8602f73350378860884df3be55cf553fee1779a0739
PS C:\Users\Jefferson Amorim> docker ps
CONTAINER ID   IMAGE                       COMMAND                  CREATED         STATUS         PORTS                                           NAMES
ca9c4e0336fa   dockersamples/static-site   "/bin/sh -c 'cd /usr…"   6 seconds ago   Up 4 seconds   0.0.0.0:49160->80/tcp, 0.0.0.0:49159->443/tcp   meusite
PS C:\Users\Jefferson Amorim> docker stop meusite
meusite
PS C:\Users\Jefferson Amorim>
```
