

import cv2
import os, shutil, pathlib

def image_editing():
    input_folder = 'img/'

    # загрузка списка файлов из папки
    files = os.listdir(input_folder)
    for file in files:
        # загрузка изображения
        img = cv2.imread(input_folder + file, 0)  # 0 чернобелое изображение

        cropped_img = img[10:1070, 430:1490]

        # сохранение обработанного изображения
        img = cv2.imwrite(input_folder + file, cropped_img)


