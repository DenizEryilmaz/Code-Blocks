import os
import zipfile

def zip_folder(folder_path, output_path):
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zip_obj:
        # Klasördeki tüm dosya ve klasörleri zip dosyasına ekleyin
        for foldername, subfolders, filenames in os.walk(folder_path):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                zip_obj.write(file_path)

# Klasörü zip dosyası olarak sıkıştırın
folder_path = "/content/gdrive/MyDrive/Results"
output_path = "/content/gdrive/MyDrive/Results.zip"
zip_folder(folder_path, output_path)