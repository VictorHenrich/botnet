# DOCUMENTAÇÃO API DE CONTROLADOR


No momento apenas um unica rota foi disponibilizada para o controle dos bots, onde para cada operação desejada é necessário preencher as informações corretamente para o funcionamento**

<h2 style="color: green"> (POST) /controlar </h2>


| Campo | Tipo | Requerido | Descrição |
| :------: | :----: | :----: | :---- |
| module | String | True | Qual dos módulos será executado, navegador, sistema operacional... |
| targets | String[] | True | Quais funcionalidades dos módulos quer ser executado |
| args | Object | True | Argumentos que serão passados para execução dos módulos |




Cada tipo de controle possui argumentos *args* que necessitam de informações para seu funcionamento, segue abaixo algumas possibilidades que podem ser trabalhadas, separados pelo módulo de funcionamento.**



### CONTROLE DE NAVEGADORES

| Campo | Tipo | Requirido | Descrição |
| :------: | :----: | :----: | :---- |
| link | String | True | Responsável pela url que será acessada |
| browser | String | True | Responsável por identificar qual browser a ser executado |
| dom | DOM[] | True | Lista de objetos que serve para manipulação de DOM no navegador |



### ***DOM***

| Campo | Tipo | Requirido | Descrição |
| :------: | :----: | :----: | :---- |
| selector | SELECTOR | True | Responsável de como se deve selecionar um dom no navegador |
| operator | OPERATOR | True | Responsável por executar alguma certa funcionalidade em relação ao dom |


### ***SELECTOR***
| Campo | Tipo | Requirido | Descrição |
| :------: | :----: | :----: | :---- |
| type | String | True | Qual tipo de seleção deve acontecer, por exemplo, por id, classe, ... |
| value | Any | True | Valor da busca para seleção |


### ***OPERATOR***

| Campo | Tipo | Requirido | Descrição |
| :------: | :----: | :----: | :---- |
| type | String | True | Qual tipo de função será executada |
| param | Any | True | Valor da busca para execução |





### CONTROLE DE SISTEMA OPERACIONAL

| Campo | Tipo | Requirido | Descrição |
| :------: | :----: | :----: | :---- |
| text | String | True | Texto a ser escrito no bloco de notas |



