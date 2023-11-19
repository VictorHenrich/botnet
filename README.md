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


Atualmente, em cada diretório (Controlador | Infectado), encontram-se arquivos com as extensões **.sh** e **.bat**. Esses arquivos contêm as instruções necessárias para a instalação, permitindo a execução das ações específicas de cada um. É importante ressaltar que a execução do controlador deve preceder a utilização dos scripts infectados, uma vez que estes dependem do controlador para operar de forma eficaz.

<br>

Os arquivos estão renomeados como `perform_in_windows.bat` para facilitar a execução no seu *CMD* / *POWERSHELL*, e `perform_in_linux.sh` para rodar em qualquer terminal Linux.

<br>

