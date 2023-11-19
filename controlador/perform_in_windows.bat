echo "Criando pasta virtual"

python -m venv venv-win

echo "Acessando pasta virtual"

call venv-win/Scripts/activate

echo "Instalando bibliotecas"

pip install -r requirements.txt

echo "Executando codigo"

python src/main.py
