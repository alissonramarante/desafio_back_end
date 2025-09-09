import os
import shutil
import datetime
import time

# Listando os arquivos e salvar no log 

source_dir = '/home/valcann/backupsFrom'
log_from_file = '/home/valcann/backupsFrom.log'

if not os.path.exists(source_dir):

    print(f"Erro: O diretório de origem {source_dir} não foi encontrado.")

else:
    with open(log_from_file, 'w') as f:

        f.write('Relatório de Arquivos - backpusFrom.log\n')
        f.write('-' * 40 + '\n')

        for filename in os.listdir(source_dir):

            file_path = os.path.join(source_dir, filename)

            if os.path.isfile(file_path):

                file_stats = os.stat(file_path)
                size_in_bytes = file_stats.st_size
                create_time = datetime.datetime.fromtimestamp(file_stats.st_ctime).strftime('%Y-%m-%d %H:%M:%S')
                modify_time = datetime.datetime.fromtimestamp(file_stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S')

                log_entry = (
                    f'Arquivo: {filename}\n'
                    f'Tamanho: {size_in_bytes} bytes\n'
                    f'Criado em: {create_time}\n'
                    f'Última modificação: {modify_time}\n'
                    f'{"-" * 40}\n'
                )
                f.write(log_entry)
    print(f"Relatório gerado com sucesso em {log_from_file}.")

# Removendo arquivos com mais de 3 dias

days_limit = 3 * 86400
current_time = time.time()

for filename in os.listdir(source_dir):
    file_path = os.path.join(source_dir, filename)

    if os.path.isfile(file_path):
        file_creation_time = os.path.getctime(file_path)

        if (current_time - file_creation_time) > days_limit:
            try:
                os.remove(file_path)
                print(f'Arquivo {filename} removido com sucesso.')
            except Exception as e:
                print(f'Erro ao remover o arquivo {filename}: {e}')

# Copiando arquivos com menos de 3 dias para outro diretório e salvando log


dest_dir = '/home/valcann/backupsTo'
log_to_file = '/home/valcann/backupsTo.log'


if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

with open(log_to_file, 'w') as f:
    f.write(f'Relatório de Cópia - backupsTo.log\n')
    f.write('-' * 40 + '\n')

    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)
        file_creation_time = os.path.getctime(file_path)

        if(current_time - file_creation_time) <= days_limit:
            try:
                shutil.copy2(file_path, dest_dir)
                log_entry = f'Arquivo {filename} copiado com sucesso.\n'
                f.write(log_entry)
                print(log_entry.strip())
            except Exception as e:
                log_entry = f'Erro ao copiar o arquivo {filename}: {e}\n'
                f.write(log_entry)
                print(log_entry.strip())

print(f'Relatório de cópia salvo em "{log_to_file}" com sucesso.')
       




