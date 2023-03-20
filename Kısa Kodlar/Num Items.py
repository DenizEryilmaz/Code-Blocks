import os

folder_path = '/folder_path'  # klasör yolunu buraya girin
num_items = len(os.listdir(folder_path))
print(f"{folder_path} klasöründe {num_items} adet öğe bulunuyor.")
