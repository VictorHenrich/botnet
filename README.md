# COMO RODAR O PYTHON NO WINDOWS


## INSTALANDO BIBLIOTECAS

### Obs: Isto é preciso ser realizado tanto nas pastas de controlador quanto de infectado para funcionar de fato, qualquer operação fora destas pasta pode comprometer o funcionamento

**Para instalar as bibliotecas necessárias para a aplicação, é necessário que seja criado um ambiente virtual, aqui iremos mostrar como fazer para criar um ambiente virtual diretamente do módulo nativo do python**

***Para criar a pasta virtual execute o seguinte comando:***

`python -m venv <nome_pasta_virtual>`

**Para instalar as outras demais bibliotecas para o funcionamento, é necessário acessar a pasta virtual para realizar a instalação a partir dele. Para acessar execute o seguinte comando:**

`<nome_pasta_virtual>/scripts/activate`


**Instale os pacotes necessários**

`(env) pip install -r requirements.txt`


## RODANDO MODULOS

**Para rodar os módulos é necessário que a instalação de seus pacotes requeridos sejam efetuados, após a instalação esta na hora de rodar nosso código. Quanto nos módulos de controlador quanto infectado precisam executar o arquivo ***main.py*** e é necessário executar o arquivo fora da pasta src (RECOMENDADO) para que algumas bibliotecas e implementações funcionem sem problemas**

`python ./src/main.py`






