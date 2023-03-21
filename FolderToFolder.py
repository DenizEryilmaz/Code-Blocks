import os
import shutil

# kaynak klasörün yolu
src_dir = '/path/to/source/folder'

# hedef klasörün yolu
dst_dir = '/path/to/destination/folder'

# kaynak klasöründeki tüm dosyaları ve alt klasörleri dolaş
for root, dirs, files in os.walk(src_dir):

    # alt klasörleri oluşturmak için hedef klasörün alt dizin yapısını koru
    dst_path = root.replace(src_dir, dst_dir, 1)

    # alt klasörleri oluştur
    for dir in dirs:
        os.makedirs(os.path.join(dst_path, dir), exist_ok=True)

    # dosyaları hedef klasöre taşı
    for file in files:
        src_file = os.path.join(root, file)
        dst_file = os.path.join(dst_path, file)
        shutil.move(src_file, dst_file)
