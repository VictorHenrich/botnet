echo "Criando pasta virtual"

python3 -m venv venv-linux

echo "Acessando pasta virtual"

source venv-linux/bin/activate

echo "Instalando bibliotecas"

pip install -r requirements.txt

echo "Executando código"

python3 src/main.py
