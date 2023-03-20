import os
import shutil

# kaynak klasörü belirle
src_folder = "/kaynak/klasör/yolu"

# hedef klasörü belirle
dst_folder = "/hedef/klasör/yolu"

# kaynak klasöründeki dosyaları listele
for file_name in os.listdir(src_folder):

    # dosya yolu oluştur
    file_path = os.path.join(src_folder, file_name)

    # dosya adının sonunda "_1.png" varsa
    if file_name.endswith("_1.png"):

        # hedef dosya yolu oluştur
        dst_path = os.path.join(dst_folder, file_name)

        # dosyayı hedef klasöre taşı
        shutil.move(file_path, dst_path)
