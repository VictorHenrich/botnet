# O QUE É UMA BOTNET?
<br>
Uma botnet é uma rede de computadores infectados que podem ser controlados remotamente e forçados a enviar spam, espalhar malware ou preparar ataques de DDoS sem o consentimento dos proprietários do dispositivo. Com o surgimento da internet das coisas a quantidade de dispositivos que podem ser infectados esse tipo de ataque está mais comum do que parece e nas mais diversas máquinas, podendo ser um perigo em potencial para grandes empresas e usuários já que atualmente praticamente tudo está conectado a rede, seja ela interna ou não.
Esta aplicação foi construida com base na arquiquetura centralizada de uma botnet, ou seja, os *bots* apenas podem ser controlados por um servidor ou computador do hacker, chamaremos esse servidor de CONTROLADOR, ele é responsável por enviar comandos as máquinas afim de executar o que queira, isso envolve controle do navegador, sistema operacional, injeção de comando shell, etc...

<br>
<br>
<br>



# COMO RODAR A APLICAÇÃO

<br>
<br>

> ## INSTALANDO BIBLIOTECAS

<br>

**Obs: Isto é preciso ser realizado tanto nas pastas de controlador quanto de infectado para funcionar de fato, qualquer operação fora destas pasta pode comprometer o funcionamento**

<br>

Para instalar as bibliotecas necessárias para a aplicação é recomendado que seja criado um ambiente virtual para alocar os módulos necessários e não inferir nos módulos globais existente em seu computador. Caso você já saiba como criar uma pasta virtual ignore o próximo passo.

<br>

### CRIANDO UMA PASTA VIRTUAL

<br>

***Para criar a pasta virtual diretamente do módulo ENV nativo do python execute o seguinte comando:***

`python -m venv <nome_pasta_virtual>`

<br>

Com a a pasta virtual criada, necessitamos acessa-la para que seja possível instalar e gerenciar os módulos dentro dela.

***Para acessar a pasta, execute o determinado comando:***

- **WINDOWS**

  `<nome_pasta_virtual>/scripts/activate`
  
- **LINUX**

  `source <nome_pasta_virtual>/bin/activate`

<br>
<br>

***Após todas os passos seguidos até aqui, seu terminal deve ficar parecido assim:***

- **WINDOWS**
> (venv) C:\pasta_projeto>

- **LINUX**
> (venv) root@user:/pasta_projeto#

<br>
<br>

### INSTALANDO OS MÓDULOS

<br>

Para instalar todos os módulos necessários para cada aplicação, você deverá instalar com base no arquivo *requirements.txt*, apartir dele que iremos requisitar nossos pacotes.

***Caso você utilize o gerenciador de pacotes PIP, execute este comando:***

`pip install -r requirements.txt`

<br>
<br>


## RODANDO MODULOS

Após a instalação dos módulos necessários e as configurações feitas, podemos já executar nossas aplicações. Para que cada coisa funcione da maneira correta, é necessário rodar primeiro a aplicação do ***CONTROLADOR*** pois será ele que irá de fato realizar a comunicação dos bots e ativar os serviços de HTTP para interação via API.

Qualquer uma das aplicações o seu funcionamento é inicializado através do arquivo *main.py* localizado dentro da pasta chamado *src* ou também conhecida como pasta *source* onde fica de fato nosso código fonte. Em nossos exemplos estamos localizados dentro da pasta raiz de cada módulo:
> /botnet-python/<controlador_ou_infectado>

<br>

***Para rodar qualquer uma das aplicações, rode o seguinte comando***:

`python ./src/main.py`






