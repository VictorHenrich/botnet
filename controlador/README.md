# DOCUMENTAÇÃO API DE CONTROLADOR

<br>
<br>

> ## *(POST)* /usuario/autenticacao

<br>

### HEADERS

* Method: POST
* Content-Type: application/json

<br>
<br>
 Esta rota é responsável por realizar a autenticação na API onde ela devolve um token que será utilizado para as demais rotas de ação e consulta.
 <br>
 <br>
 
 | Campo | Tipo | Requerido | Descrição |
| :------: | :----: | :----: | :---- |
| email | String | True | Email de acesso |
| senha | String[] | True | Senha de acesso |

<br>

### EXEMPLO CORPO JSON

 ```
 {
	"email": "fulano@gmail.com",
	"senha": "*******"
 }
 ```

<br>

### EXEMPLO RESPOSTA SUCESSO

 ```
 {
	"status": 200,
	"message": "OK",
	"result": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiN2NkYmQ3MzgtMjg1OC00YTQ4LWJhMmUtYTc4ZTZkYjE5M2Y3IiwiZXhwaXJlZCI6MTY2NzkxNTUwMy42NzUyOTZ9.c8uiHYy52FcqIZ0Aqytmzf97nV0mBmUz7nvYHJURKeo"
}
 ```

<br>
<br>
<br>
<br>

> ## *(POST)* /usuario/cadastro

<br>

### HEADERS

* Method: POST
* Content-Type: application/json

<br>
<br>
 Esta rota é responsável por cadastrar um novo usuário no banco de dados.
 <br>
 <br>
 
 | Campo | Tipo | Requerido | Descrição |
| :------: | :----: | :----: | :---- |
| email | String | True | Email de acesso |
| senha | String[] | True | Senha de acesso |

<br>

### EXEMPLO CORPO JSON

 ```
 {
	"email": "fulano@gmail.com",
	"senha": "*******"
 }
 ```

<br>

### EXEMPLO RESPOSTA SUCESSO

 ```
 {
	"status": 200,
	"message": "OK"
}
 ```

<br>
<br>
<br>
<br>

> ## *(PUT)* /usuario/cadastro

<br>

### HEADERS

* Method: POST
* Content-Type: application/json
* Authorization: Bearer <TOKEN>

<br>
<br>
 Esta rota é responsável por alterar os dados de um usuário no banco de dados.
 <br>
 <br>
 
 | Campo | Tipo | Requerido | Descrição |
| :------: | :----: | :----: | :---- |
| email | String | True | Email de acesso |
| senha | String[] | True | Senha de acesso |

<br>

### EXEMPLO CORPO JSON

 ```
 {
	"email": "fulano@gmail.com",
	"senha": "*******"
 }
 ```

<br>

### EXEMPLO RESPOSTA SUCESSO

 ```
 {
	"status": 200,
	"message": "OK"
}
 ```

<br>
<br>
<br>
<br>

> ## *(DELETE)* /usuario/cadastro

<br>

### HEADERS

* Method: POST
* Content-Type: application/json
* Authorization: Bearer <TOKEN>

<br>
<br>
 Esta rota é responsável por excluir os dados de um usuário no banco de dados.
 <br>
 <br>
 
 | Campo | Tipo | Requerido | Descrição |
| :------: | :----: | :----: | :---- |
| email | String | True | Email de acesso |
| senha | String[] | True | Senha de acesso |

<br>

### EXEMPLO CORPO JSON

 ```
 {
	"email": "fulano@gmail.com",
	"senha": "*******"
 }
 ```

<br>

### EXEMPLO RESPOSTA SUCESSO

 ```
 {
	"status": 200,
	"message": "OK"
}
 ```

<br>
<br>
<br>
<br>


> ## *(POST)* /bots/controlar

<br>

Este módulo visa o controle sobre os bots, onde é possível desde o controle completo do navegador até operações realizadas em sistemas operacionais ou diretamente da máquina. Para vocÇe conseguir de fato utilizar esta rota é necessário primeiramente a autenticação para conseguir pegar o *TOKEN* que será utilizado para identificar o controlador.
<br>

### HEADERS
  
* Method: POST
* Content-Type: application/json
* Authorization: ***TOKEN***

<br>

| Campo | Tipo | Requerido | Descrição |
| :------: | :----: | :----: | :---- |
| module | String | True | Qual dos módulos será executado, navegador, sistema operacional... |
| targets | String[] | True | Quais funcionalidades dos módulos quer ser executado |
| args | Object | True | Argumentos que serão passados para execução dos módulos |

<br>


Cada tipo de controle possui argumentos *args* que necessitam de informações para seu funcionamento, segue abaixo algumas possibilidades que podem ser trabalhadas, separados pelo módulo de funcionamento.

<br>
<br>

### CONTROLE DE NAVEGADORES
<br>
**Este módulo revisa o controle do navegador através dos bots (Infectados), onde é possivel informar qual site o navegador deve acessar como também quais elementos *HTML* serão selecionados e ativados a realizar alguma determinada ação.**
<br>

| Campo | Tipo | Requirido | Descrição |
| :------: | :----: | :----: | :---- |
| link | String | True | Responsável pela url que será acessada |
| browser | String | True | Responsável por identificar qual browser a ser executado |
| dom | Array<***DOM***> | True | Lista de objetos que serve para manipulação de DOM no navegador |

<br>

#### *DOM*

| Campo | Tipo | Requirido | Descrição |
| :------: | :----: | :----: | :---- |
| selector | ***SELECTOR*** | True | Responsável de como se deve selecionar um dom no navegador |
| operator | ***OPERATOR*** | True | Responsável por executar alguma certa funcionalidade em relação ao dom |

<br>

#### *SELECTOR*
| Campo | Tipo | Requirido | Descrição |
| :------: | :----: | :----: | :---- |
| type | String | True | Qual tipo de seleção deve acontecer, por exemplo, por id, classe, ... |
| value | Any | True | Valor da busca para seleção |

<br>

#### *OPERATOR*

| Campo | Tipo | Requirido | Descrição |
| :------: | :----: | :----: | :---- |
| type | String | True | Qual tipo de função será executada |
| param | Any | True | Valor da busca para execução |

<br>
<br>

### EXEMPLO CORPO JSON

 ```
 {
		"module":"automacao_navegador",
		"targets": ["abrir_pagina"],
		"args": {
			"link": "https://youtube.com.br",
			"browser": "chrome",
			"dom":[
				{
					"selector":{
						"type": "tag",
						"value": "input"
					},
					"operator": {
						"type": "write",
						"param": "Digitar isso no campo de busca"
					}
				}
			]
		}
}
 ```

<br>
<br>
<br>

### CONTROLE DE SISTEMA OPERACIONAL
<br>
Este modulo revisa o controle do computador em si do usuário. Nesta primeira parte da implementação o usuário apenas irá conseguir abrir o bloco de notas do bot.
<br>
<br>

| Campo | Tipo | Requirido | Descrição |
| :------: | :----: | :----: | :---- |
| text | String | True | Texto a ser escrito no bloco de notas |

<br>
<br>

 ```
 {
		"module":"automacao_so",
		"targets": ["abrir_bloco_notas"],
		"args": {
			"text": "Digite isso aqui no bloco de notas"
		}
}

 ```



