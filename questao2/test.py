import json
import os
from pathlib import Path
import datetime

# Caminhos usados pelo automacao.py
source_dir = '/home/valcann/backupsFrom'
Path(source_dir).mkdir(parents=True, exist_ok=True)

# Carregar o JSON (seu mock-users.json)
with open('mock-users.json', 'r') as f:
    usuarios = json.load(f)

# Criar arquivos simulados para cada usuário do JSON
for user in usuarios:
   
    nome_arquivo = f"{user['id']}_{user['name'].replace(' ', '_')}.txt"
    conteudo = (
        f"Nome: {user['name']}\n"
        f"Email: {user['email']}\n"
        f"Role: {user['role']}\n"
        f"Ativo: {user['is_active']}\n"
        f"Criado em: {user['created_at']}\n"
    )
    caminho_arquivo = os.path.join(source_dir, nome_arquivo)
    with open(caminho_arquivo, 'w') as arq:
        arq.write(conteudo)

    dt = datetime.datetime.fromisoformat(user['created_at'].replace('Z', '+00:00'))
    timestamp = dt.timestamp()
    os.utime(caminho_arquivo, (timestamp, timestamp))

print("Arquivos simulados criados com sucesso.")
import automacao
print("Execução do automacao.py concluída. Verifique backupsFrom.log e backupsTo.log.")