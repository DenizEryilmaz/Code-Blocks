import zipfile
zip_ref = zipfile.ZipFile("/content/gdrive/MyDrive/X.zip", 'r')
zip_ref.extractall("/content/gdrive/MyDrive/X")
zip_ref.close()