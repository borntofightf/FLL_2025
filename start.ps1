# start.ps1
# Ativa o ambiente virtual
& .\.venv\Scripts\Activate.ps1

# Garante que pip está atualizado
python -m pip install --upgrade pip

# Instala as dependências se não estiverem instaladas
pip install -r requirements.txt

Write-Host "Ambiente pronto! Agora você pode usar pybricksdev."
