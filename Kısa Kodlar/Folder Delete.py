import os
import shutil

klasor_yolu = 'c:/filepath'

try:
    shutil.rmtree(klasor_yolu)

except OSError as e:
    print(f'Hata: {klasor_yolu} silinemedi: {e}')
