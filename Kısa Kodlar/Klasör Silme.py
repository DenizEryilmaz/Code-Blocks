import os
import shutil

klasor_yolu = ''

try:
    shutil.rmtree(klasor_yolu)

except OSError as e:
    print(f'Hata: {klasor_yolu} silinemedi: {e}')
