import os

# Dossier contenant les fichiers .txt
folder_path = './images/2024'
# Chemin du fichier de sortie
output_file = 'train.txt'
# Préfixe à ajouter devant chaque nom d'image
prefix = 'data/obj_train_data/'

# Récupérer tous les fichiers .txt dans le dossier
txt_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]

# Convertir les noms en noms .jpg avec le bon chemin
jpg_paths = [prefix + os.path.splitext(f)[0] + '.jpg' for f in txt_files]

# Écrire dans train.txt
with open(output_file, 'w') as f:
    for path in jpg_paths:
        f.write(path + '\n')

print(f"{len(jpg_paths)} lignes écrites dans {output_file}.")
